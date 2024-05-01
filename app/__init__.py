from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from config import Config

db = SQLAlchemy()
migrate = Migrate()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app, db)

    from .models import State, City, Category, Item, User, Address, UserItemSaved, ItemAuction, Comment, Bid, Photo, UserItemSaved

    from .auth import create_module as auth_create_module
    from .main import create_module as main_create_module
    from .me import create_module as me_create_module
    from .item import create_module as item_create_module

    auth_create_module(app)
    main_create_module(app)
    me_create_module(app)
    item_create_module(app)

    @app.route("/test")
    def test():
        return "<div>Hello, World!</div>"

    # blue prints

    return app