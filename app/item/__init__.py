from flask import Flask

def create_module(app: Flask):
    from .routes import item_blueprint
    app.register_blueprint(item_blueprint)