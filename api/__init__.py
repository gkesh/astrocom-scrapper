import os
from quart import Quart
from quart_motor import Motor
from flask_mongoengine import MongoEngine


app: Quart = Quart(__name__)
# Mongo Config
db: str = os.getenv("DB_NAME")
host: str = os.getenv("DB_HOST")
port: str = os.getenv("DB_PORT")

app.config["MONGO_URI"] = f"mongodb://{host}:{port}/{db}"

db = Motor(app)