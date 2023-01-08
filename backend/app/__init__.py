from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from .views import views

db = SQLAlchemy()
DB_NAME = "database.db"


def create_app():
    app = Flask(__name__)
    app.register_blueprint(views, url_prefix='/')
    return app


def create_database(app):
    if not path.exists('website/' + DB_NAME):
        db.create_all(app=app)
        print('Created Database!')
