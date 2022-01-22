from flask import Flask
from flask_mongoengine import MongoEngine

app: Flask = Flask(__name__)
app.config["MONGODB_SETTINGS"] = {
    'db': 'astrocom',
    'host': 'localhost',
    'port': 27017
}

db: MongoEngine = MongoEngine()
db.init_app(app)

@app.route('/')
def info() -> str:
    return "Welcome to Astrocom Scrapper v0.5"