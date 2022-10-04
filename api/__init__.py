"""
The api module handles all operations
related to the database calls as well
as the graphql operations.

The module will be slightly coupled to
the engine module but won't depend on it
completely to function.

@author gkesh
"""

from os import getenv as env
from flask import Flask
from flask_mongoengine import MongoEngine


NAME = "API"

app: Flask = Flask(__name__)
app.config["MONGODB_SETTINGS"] = {
    'db': env("DB_NAME"),
    'host': env("DB_HOST"),
    'port': int(env("DB_PORT"))
}
app.config['CORS_HEADERS'] = ['Content-Type', 'Access-Control-Allow-Origin']
app.config['CORS_ORIGINS'] = '*'

db: MongoEngine = MongoEngine()
db.init_app(app)