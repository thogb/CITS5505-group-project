from flask import (Blueprint, render_template)

auth_blueprint = Blueprint('auth', __name__, template_folder='templates')

@auth_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('auth/login.html')

@auth_blueprint.route("/register", methods=['GET', 'POST'])
def register():
    pass

@auth_blueprint.route("/logout", methods=['GET', 'POST'])
def logout():
    pass

