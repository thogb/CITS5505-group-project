from flask import (Blueprint, flash, redirect, render_template, url_for)

from app.auth.forms import LoginForm, RegisterForm
from app.models import User
from app import db

auth_blueprint = Blueprint('auth', __name__, template_folder='templates')

@auth_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    return render_template('auth/login.html', form=form)

@auth_blueprint.route("/register", methods=['GET', 'POST'])
def register():
    form = RegisterForm()

    print(form.email)
    print(form.first_name)
    print(form.last_name)
    print(form.password)
    print(form.confirm_password)
    print(form.validate_on_submit())

    if form.validate_on_submit():
        user = User(email=form.email.data,
                     first_name=form.first_name.data,
                       last_name=form.last_name.data,
                         password=form.password.data)
        user.set_password(form.password.data)

        db.session.add(user)
        db.session.commit()

        flash("Successfully created user", category="success")

        return redirect(url_for('auth.login'))

    return render_template("auth/register.html", form=form)

@auth_blueprint.route("/logout", methods=['GET', 'POST'])
def logout():
    pass

