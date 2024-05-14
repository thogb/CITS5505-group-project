from flask import Flask

def create_module(app: Flask):
    from .routes import item_blueprint
    from .api_controller import item_api_blueprint
    app.register_blueprint(item_blueprint)
    app.register_blueprint(item_api_blueprint)