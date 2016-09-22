from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

import config
import logging
import connexion

application = connexion.App(__name__, specification_dir='swagger/')
application.add_api('rest_api_doc.yml')

app = application.app
app.config.from_object(config)


db = SQLAlchemy(app)
migrate = Migrate(app, db)

logging.basicConfig(filename=config.LOG_FILE_PATH, level=logging.DEBUG)


