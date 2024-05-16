from flask import (Blueprint, render_template)
from flask_login import login_required
from sqlalchemy import func
from sqlalchemy.orm import joinedload
from app import awsS3_service


from app.models import Item
from app.services.category import getAllCategories

main_blueprint = Blueprint('main', __name__, template_folder='../templates/home')

@main_blueprint.before_request
@login_required
def before_request():
    return

@main_blueprint.route('/', methods=['GET'])
def home():
    categories = getAllCategories();

    # Get random 4 items
    items = Item.query\
        .filter_by(sold_time=None, delete_time=None)\
        .options(joinedload(Item.photos))\
        .order_by(func.random())\
        .limit(4)\
        .all()
    
    for item in items:
        photo = len(item.photos) > 0 and item.photos[0]
        if photo:
            item.thumb_photo_url = awsS3_service.generate_presigned_url(f"{photo.id}.{photo.extension}")
    
    return render_template('home.html', categories=categories, items=items)