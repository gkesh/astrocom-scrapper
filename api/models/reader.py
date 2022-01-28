from api import db
from datetime import datetime

class Reader(db.Document):
    _id = db.ObjectIdField()
    username = db.StringField(max_length=200, required=True)
    email = db.EmailField(domain_whitelist=["gmail.com", "hotmail.com", "outlook.com", "apple.com"])
    date_birthed = db.DateTimeField(required=True)
    date_joined = db.DateTimeField(default=datetime.utcnow)

    def to_dict(self) -> dict:
        return {
            "id": str(self._id),
            "username": self.username,
            "email": self.email,
            "date_birthed": str(self.date_birthed.strftime('%d-%m-%Y')),
            "date_joined": str(self.date_joined.strftime('%d-%m-%Y'))
        }