from flaskext.sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine


db = SQLAlchemy()


def init_app(app):
    """Initializes Flask app."""
    db.app = app
    db.init_app(app)
    return db


def create_tables(app):
    "Create tables, and return engine in case of further processing."
    engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'])
    db.metadata.create_all(engine)
    return engine


class Spam(db.Model):
    __tablename__ = 'spams'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(16))


class Egg(db.Model):
    __tablename__ = 'eggs'

    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.Text)
