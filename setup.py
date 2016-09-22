from setuptools import setup


# Tested on Python 2.6 using the packages below.

setup(
    name='FlaskFixtures',
    install_requires=[
        'fixture',
        'Flask',
        'Flask-Script',
        'Flask-SQLAlchemy>=1.0',
        'Flask-Testing',
        'SQLAlchemy',
        'connexion',
        'flask-migrate',
        'mixer',
        'fake-factory>=0.5.0',
        ],
    )
