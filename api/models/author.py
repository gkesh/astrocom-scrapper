from api import db
from api.models import ReusableDocument


class Author(ReusableDocument, db.Document):
    """
    Author Class
    """
    _id = db.ObjectIdField()
    first_name = db.StringField(max_length=200, required=True)
    last_name = db.StringField(max_length=200, required=True)
    biography = db.StringField(required=False)

    def to_dict(self) -> dict:
        return {
            "id": str(self._id),
            "first_name": self.first_name,
            "last_name": self.last_name,
            "biography": self.biography
        }
