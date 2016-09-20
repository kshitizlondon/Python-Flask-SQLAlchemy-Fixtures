from flask import Flask

import config
import models


app = Flask(__name__)
app.config.from_object(config)

db = models.init_app(app)
