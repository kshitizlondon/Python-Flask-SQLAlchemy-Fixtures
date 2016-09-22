Kshitiz Mahajan

Demonstrate use of ``fixture`` with Flask-SQLAlchemy and Flask-Testing.


Setup
-----

To create the virtualenv:
```bash
$ python3 -m venv bac-env
```
To activate:
```bash
$ source bac-env/bin/activate
```

To install dependencies:
```bash
$ pip3 install -r requirements.txt
```


Get this::

    git clone git@github.com:kshitizlondon/Python-Flask-SQLAlchemy-Fixtures.git
    cd Python-Flask-SQLAlchemy-Fixtures

To run, activate a virtualenv and::

    python setup.py develop
    python test_models.py

If you don't like DeprecationWarning, you can::

    python -W ignore::DeprecationWarning test_models.py

You can also::

    python manage.py fixtures
    sqlite3 app.db

In sqlite3::

    .schema
    select * from spams;
    select * from eggs;



Also install Sqlite3 on your local machine if not using any Virtualization like docker, vagrant, chef etc ::
