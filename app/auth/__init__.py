from flask import Flask

def create_module(app: Flask):
    from .routes import auth_blueprint
    app.register_blueprint(auth_blueprint)