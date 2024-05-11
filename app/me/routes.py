from flask import (Blueprint, abort, flash, redirect, render_template, request, url_for)
from flask_login import current_user, login_required
from app import db  
from app.me.forms import ProfileForm
from app.models import Address, Item, User, UserItemSaved
from app import awsS3_service
from app.services.city import checkIfCityExists, getCities
from app.shared.base_filtering_parameters import BaseFilteringParameters

me_blueprint = Blueprint('me', __name__, template_folder='templates' , url_prefix="/me")

@me_blueprint.before_request
@login_required
def before_request():
    return

@me_blueprint.route('/', methods=['GET', 'POST'])
def me():
    form = ProfileForm()
    form.city.choices = [(city.id, city.name) for city in getCities()]

    if form.validate_on_submit():
        user = current_user

        user.email = form.email.data
        user.phone_number = form.phone_number.data
        user.first_name = form.first_name.data
        user.last_name = form.last_name.data

        if not checkIfCityExists(form.city.data):
            flash("Invalid city", category="danger")
            return redirect(url_for('me.me'))

        
        if not user.address:
            address = Address(
                address = form.address.data,
                city_id = form.city.data
            )
            user.address = address
            # db.session.add(address)x

        user.address.address = form.address.data
        user.address.city_id = form.city.data

        db.session.commit()

        redirect(url_for('me.me'))

    if form.phone_number.errors:
        flash(form.phone_number.errors[0], category="danger")
        return render_template('me/me.html', form=form)

    form.email.data = current_user.email
    form.phone_number.data = current_user.phone_number
    form.first_name.data = current_user.first_name
    form.last_name.data = current_user.last_name

    if current_user.address:
        form.address.data = current_user.address.address
        form.city.data = current_user.address.city_id
        

    return render_template('me/me.html', form=form)

@me_blueprint.route('/saved', methods=['GET'])
@me_blueprint.route('/saved/', methods=['GET'])
def saved():
    filter = BaseFilteringParameters()
    filter.from_request(request)
    
    saved_items = UserItemSaved\
        .query\
        .filter_by(user_id=current_user.id)\
        .order_by(UserItemSaved.create_time.desc())\
        .paginate(page=filter.page, per_page=filter.per_page)

    for saved_item in saved_items:
        if len(saved_item.item.photos) > 1:
            thumb_photo = saved_item.item.photos[0]
            saved_item.item.thumb_photo_url = awsS3_service.generate_presigned_url(f"{thumb_photo.id}.{thumb_photo.extension}")

    return render_template('me/saved.html', saved_items=saved_items, filter=filter)

@me_blueprint.route('/items', methods=['GET'])
def items():
    filter = BaseFilteringParameters()
    filter.from_request(request)

    items = Item.query\
        .filter_by(user_id=current_user.id)\
        .order_by(Item.create_time.desc())\
        .paginate(page=filter.page, per_page=filter.per_page)
    
    for item in items:
        if len(item.photos) > 1:
            thumb_photo = item.photos[0]
            item.thumb_photo_url = awsS3_service.generate_presigned_url(f"{thumb_photo.id}.{thumb_photo.extension}")

    return render_template('me/items.html', items=items, filter=filter)

@me_blueprint.route('/bids', methods=['GET'])
def bids():
    return render_template('me/bids.html')