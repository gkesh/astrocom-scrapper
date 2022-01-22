from flask_mongoengine import Document
from api import db
from datetime import datetime

class Reader(db.Document):
    username = db.StringField(max_length=200, required=True)
    avatar = db.ImageField(size=(200, 200, True), thumbnail_size=(50, 50, True))
    email = db.EmailField(domain_whitelist=["gmail.com", "hotmail.com", "outlook.com", "apple.com"])
    date_birthed = db.DateTimeField(required=True)
    date_joined = db.DateTimeField(default=datetime.utcnow)

    def to_dict(self) -> dict:
        return {
            "username": self.username,
            "email": self.email,
            "date_birthed": self.date_birthed,
            "date_joined": self.date_joined
        }