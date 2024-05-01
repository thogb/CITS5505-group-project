from flask import Flask

def create_module(app: Flask):
    from .routes import me_blueprint
    app.register_blueprint(me_blueprint)