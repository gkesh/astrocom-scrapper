import os
from flask import Flask
from flask_mongoengine import MongoEngine


app: Flask = Flask(__name__)
app.config["MONGODB_SETTINGS"] = {
    'db': os.getenv("DB_NAME"),
    'host': os.getenv("DB_HOST"),
    'port': int(os.getenv("DB_PORT"))
}
app.config['CORS_HEADERS'] = ['Content-Type', 'Access-Control-Allow-Origin']
app.config['CORS_ORIGINS'] = '*'

db: MongoEngine = MongoEngine()
db.init_app(app)