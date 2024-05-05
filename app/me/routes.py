from flask import (Blueprint, render_template)
from flask_login import current_user, login_required
from app import db  
from app.me.forms import ProfileForm
from app.models import User
from app.services.city import getCities

me_blueprint = Blueprint('me', __name__, template_folder='templates' , url_prefix="/me")

@me_blueprint.before_request
@login_required
def before_request():
    return

@me_blueprint.route('/', methods=['GET', 'POST'])
def me():
    form = ProfileForm()

    if form.validate_on_submit():
        user = User.query.filter_by(id=current_user.id).first()

        user.email = form.email.data
        user.phone_number = form.phone_number.data
        user.first_name = form.first_name.data
        user.last_name = form.last_name.data
        user.address.address = form.address.data
        user.address.city_id = form.city.data

        db.session.commit()

    form.email.data = current_user.email
    form.phone_number.data = current_user.phone_number
    form.first_name.data = current_user.first_name
    form.last_name.data = current_user.last_name
    form.city.choices = [(city.id, city.name) for city in getCities()]
    for city in getCities():
        print(city.state_id)

    if current_user.address:
        form.address.data = current_user.address.address
        form.city.data = current_user.address.city
        

    return render_template('me/me.html', form=form)