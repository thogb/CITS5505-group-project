from functools import wraps
from flask import (Blueprint, flash, redirect, render_template, request, url_for)
from flask_login import current_user, login_required, login_user, logout_user

from app.auth.forms import LoginForm, RegisterForm
from app.models import User
from app import db

auth_blueprint = Blueprint('auth', __name__, template_folder='templates')

def only_anonymous(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if current_user.is_authenticated:
            # return redirect(url_for('login', next=request.url))
            return redirect(url_for('main.home'))
        return f(*args, **kwargs)
    
    return decorated_function

@auth_blueprint.route('/login', methods=['GET', 'POST'])
@only_anonymous
def login():
    form = LoginForm()
    
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()

        if not user or not user.check_password(form.password.data):
            flash("Invalid email or password", category="danger")
            return redirect(url_for('auth.login'))
        
        login_user(user)

        flash("Successfully logged in", category="success")

        next = request.args.get('next')

        return redirect(next or url_for('main.home'))

    return render_template('auth/login.html', form=form)

@auth_blueprint.route("/register", methods=['GET', 'POST'])
@only_anonymous
def register():
    form = RegisterForm()

    # TODO: remove
    print(form.email)
    print(form.first_name)
    print(form.last_name)
    print(form.password)
    print(form.confirm_password)
    print(form.validate_on_submit())

    if form.validate_on_submit():
        check_user = User.query.filter_by(email=form.email.data).first()

        if check_user:
            flash("User already exists", category="danger")
            return redirect(url_for('auth.register'))

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
@login_required
def logout():
    logout_user()
    flash("Successfully logged out", category="success")

    return redirect(url_for('auth.login'))

