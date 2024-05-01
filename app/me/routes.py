from flask import (Blueprint)

me_blueprint = Blueprint('me', __name__, template_folder='templates' , url_prefix="/me")