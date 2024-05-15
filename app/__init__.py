from flask import Flask, abort, request
from flask_caching import Cache
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from .services.awsS3 import AWSS3

from config import Config

# Retrieved from https://stackoverflow.com/questions/62640576/flask-migrate-valueerror-constraint-must-have-a-name
# Date: 11/05/2024

convention = {
    "ix": 'ix_%(column_0_label)s',
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}

metadata = MetaData(naming_convention=convention)

db = SQLAlchemy(metadata=metadata)
migrate = Migrate()
cache = Cache()
awsS3_service = AWSS3()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app, db)
    cache.init_app(app)
    awsS3_service.create_from_app(app, cache=cache)

    from .models import State, City, Category, Item, User, Address, UserItemSaved, ItemAuction, Comment, Bid, Photo, UserItemSaved

    from .auth import create_module as auth_create_module
    from .main import create_module as main_create_module
    from .me import create_module as me_create_module
    from .item import create_module as item_create_module

    auth_create_module(app)
    main_create_module(app)
    me_create_module(app)
    item_create_module(app)

    @app.route("/test",)
    def test():
        return "<div>Hello, World!</div>"

    @app.route("/test-two", methods=["GET"])
    def test_two():
        print(request.is_json)
        print("test")
        return "test two"

    # blue prints

    return app