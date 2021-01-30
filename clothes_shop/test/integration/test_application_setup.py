"""Testing the integration of our application setup and its interaction with our database"""

import os

import pytest
from sqlalchemy.exc import ProgrammingError

from clothes_shop import application_setup


def test_application_setup():
    """Checking the database connection is active with correction details"""
    table_name = "clothes_stock"

    app, db = application_setup.application_setup()

    assert app.config["SQLALCHEMY_DATABASE_URI"] == str(db.session.bind.url)
    assert db.session.execute(f"SELECT * from {table_name}")


def test_application_setup_with_incorrect_password():
    """Check database connection throws ProgrammingError using incorrect password"""
    table_name = "clothes_stock"
    os.environ["PG_PASSWORD"] = "incorrect_password"

    app, db = application_setup.application_setup()

    assert app.config["SQLALCHEMY_DATABASE_URI"] == str(db.session.bind.url)

    with pytest.raises(ProgrammingError):
        db.session.execute(f"SELECT * from {table_name}")


def test_application_setup_with_invalid_user():
    """Check database connection throws a ProgrammingError when an invalid user is used"""
    table_name = "clothes_stock"
    os.environ["PG_USERNAME"] = "invalid_user"

    app, db = application_setup.application_setup()

    assert app.config["SQLALCHEMY_DATABASE_URI"] == str(db.session.bind.url)

    with pytest.raises(ProgrammingError):
        db.session.execute(f"SELECT * from {table_name}")
