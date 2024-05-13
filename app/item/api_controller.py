from flask import Blueprint
from app.decorators.only_json import validate_json
from app.item.service import ItemService

item_api_blueprint = Blueprint('item_api', __name__, template_folder='templates', url_prefix="/api/items")

@item_api_blueprint.before_request
@validate_json
def before_request():
    return

@item_api_blueprint.route('/<int:item_id>/save/<int:save_status>', methods=['POST'])
# @validate_json
def item_save(item_id, save_status):
    return ItemService.save(item_id, save_status);

@item_api_blueprint.route("/<int:item_id>/request", methods=['POST'])
def send_request(item_id):
    return ItemService.send_request(item_id)

@item_api_blueprint.route("/<int:item_id>/request/<int:item_request_id>/respond", methods=['POST'])
def respond_request(item_id, item_request_id):
    return ItemService.respond_item_request(item_id, item_request_id)