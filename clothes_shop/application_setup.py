"""Application Setup"""

import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy


def application_setup():
    """Create a Flask application and initialise the clothes shop database"""

    username = os.environ.get("PG_USERNAME", "alex")
    password = os.environ.get("PG_PASSWORD", "test")
    database_name = os.environ.get("DATABASE_NAME", "clothes_shop")

    _app = Flask(__name__)
    _app.config["SQLALCHEMY_DATABASE_URI"] = f"postgresql+pg8000://{username}:{password}@localhost:5432/{database_name}"
    _app.config["SQLALCHEMY_BINDS"] = {database_name:  _app.config["SQLALCHEMY_DATABASE_URI"]}
    _app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db = SQLAlchemy(_app)
    db.init_app(_app)

    return _app, db

