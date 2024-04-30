from flask import (Blueprint)

item_blueprint = Blueprint('item', __name__, template_folder='templates', url_prefix="/item")