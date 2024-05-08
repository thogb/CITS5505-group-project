from multiprocessing.pool import ThreadPool
from flask import (Blueprint, flash, redirect, render_template, request, url_for)
from flask_login import current_user, login_required
from app import db
from app.decorators.only_json import validate_json
from app.item.forms import NewItemForm
from app.item.items_filtering_parameters import ItemFilteringParameters
from app.item.service import ItemService
from app.models import Item, Photo, UserItemSaved
from app import awsS3
from app.services.category import getAllCategories
from app.services.city import getCities
from sqlalchemy.orm import joinedload

item_blueprint = Blueprint('item', __name__, template_folder='templates', url_prefix="/items")

@item_blueprint.before_request
@login_required
def before_request():
    return

@item_blueprint.route('/', methods=['GET', 'POST'])
def items():
    filter = ItemFilteringParameters()
    filter.from_request(request)

    query = filter.getQuery(Item.query.order_by(Item.create_time.desc()))
    query = query.options(joinedload(Item.photos))
    items = query.paginate(
        page=filter.page,
        per_page=filter.per_page
    )

    item_ids = [ item.id for item in items.items ]
    
    # Find out which items are saved by the user
    if len(item_ids) > 0:
        user_item_saved = UserItemSaved\
            .query\
            .with_entities(UserItemSaved.item_id)\
            .filter(UserItemSaved.item_id.in_(item_ids), UserItemSaved.user_id == current_user.id)\
            .all()
        saved_item_id_set = set([ item.item_id for item in user_item_saved ])
        print(saved_item_id_set)
        for item in items.items:
            item.saved_by_user = item.id in saved_item_id_set

    # for item in items:
    #     photo = len(item.photos) > 0 and item.photos[0]
    #     if photo:
    #         # photo.photo_url = awsS3.generate_presigned_url(f"{photo.id}.{photo.extension}")
    #         item.thumb_photo_url = awsS3.generate_presigned_url(f"{photo.id}.{photo.extension}")

    return render_template('item/items.html', items=items, filter=filter)

@item_blueprint.route('/<int:item_id>', methods=['GET'])
def item(item_id):
    item = Item.query.get_or_404(item_id)
    
    for photo in item.photos:
        photo.photo_url = awsS3.generate_presigned_url(f"{photo.id}.{photo.extension}")

    return render_template('item/item.html', item=item)

@item_blueprint.route('/<int:item_id>/save/<int:save_status>', methods=['POST'])
@validate_json
def item_save(item_id, save_status):
    return ItemService.save(item_id, save_status);

@item_blueprint.route('/new', methods=['GET', 'POST'])
def item_new():
    form = NewItemForm()

    form.city.choices = [(city.id, city.name) for city in getCities()]
    form.category.choices = [(category.id, category.name) for category in getAllCategories()]
    print(getAllCategories())

    if form.validate_on_submit():
        try:
            # Make sure all data are added correctly else rollback
            with db.session.begin_nested():
                item = Item(
                    title=form.title.data,
                    city_id=form.city.data,
                    category_id=form.category.data,
                    used=form.used.data,
                    description=form.description.data,
                    user_id=current_user.id,
                    price=form.price.data
                )

                all_photos = []

                for photo in form.photos.data:
                    extension = photo.filename.split('.')[-1]
                    all_photos.append(
                        Photo(
                            original_name=photo.filename,
                            extension=extension,
                            photo_file=photo
                        )
                    )
                item.photos = all_photos

                db.session.add(item)
            db.session.commit()

            for photo in all_photos:
                awsS3.upload_file(photo.photo_file, f"{photo.id}.{photo.extension}")

            flash("Item created successfully", "success")
            # TODO: redirect to the item or not
            return redirect(url_for('main.home'))
        except Exception as e:
            print(e)
            flash("Error creating item", "error")
            db.session.rollback()
            return render_template('item/item-new.html', form=form)
        
    if form.errors:
        for field, errors in form.errors.items():
            for error in errors:
                flash(error, "error") 

    return render_template('item/item-new.html', form=form)