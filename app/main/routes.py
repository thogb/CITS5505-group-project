from flask import (Blueprint, render_template)
from flask_login import login_required

main_blueprint = Blueprint('main', __name__, template_folder='../templates/home')

@main_blueprint.before_request
@login_required
def before_request():
    return

@main_blueprint.route('/', methods=['GET'])
def home():
    return render_template('home.html')