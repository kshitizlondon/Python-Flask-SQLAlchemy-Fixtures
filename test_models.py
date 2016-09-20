import unittest

from flask import Flask
from unittest

import fixtures
import models


class ModelsTestCase(unittest.TestCase):

    db_uri = "sqlite:///tests.db"

    def create_app(self):
        app = Flask(__name__)
        app.config['SQLALCHEMY_DATABASE_URI'] = self.db_uri
        return app

    def setUp(self):
        models.create_tables(self.app)
        fixtures.install(self.app, *fixtures.all_data)
        self.db = models.init_app(self.app)

    def tearDown(self):
        self.db.session.remove()
        self.db.drop_all()

    def test_spam(self):
        spam = models.Spam.query.first()
        self.assertEquals(spam.name, 'spam spam spam')

    def test_egg(self):
        egg = models.Egg.query.first()
        self.assertTrue(egg.description.startswith('green'))


if __name__ == '__main__':
    unittest.main()
