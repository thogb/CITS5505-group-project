from flask import Flask
from flask_login import LoginManager

login_manager = LoginManager()
login_manager.login_view = 'auth.login'


def create_module(app: Flask):
    from .routes import auth_blueprint
    app.register_blueprint(auth_blueprint)

    login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    from ..models import User
    return User.query.get(int(user_id))