from api import db
from api.models import ReusableDocument


class Genre(ReusableDocument, db.Document):
    """
    Genre Class

    The genre defines the category any creation
    belongs to and helps identify its nature
    """
    _id = db.ObjectIdField()
    name = db.StringField(max_length=100, required=True, unique=True)
    description = db.StringField(required=True)

    def to_dict(self) -> dict:
        return {
            "id": self._id,
            "name": self.name,
            "description": self.description
        }
