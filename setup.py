from setuptools import setup


# Tested on Python 2.6 using the packages below.

setup(
    name='FlaskFixtures',
    install_requires=[
        'fixture',
        'Flask',
        'Flask-Script',
        'Flask-SQLAlchemy<0.10',
        'Flask-Testing',
        'SQLAlchemy',
        ],
    )
