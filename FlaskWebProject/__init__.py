"""
The flask application package.
"""

from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config.from_object(Config)
# # TODO: Add any logging levels and handlers with app.logger

db = SQLAlchemy(app)

import FlaskWebProject.views