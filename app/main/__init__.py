from flask import Flask

def create_module(app: Flask):
    from .routes import main_blueprint
    app.register_blueprint(main_blueprint)