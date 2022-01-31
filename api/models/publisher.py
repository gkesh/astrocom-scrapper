from api import db


class Publisher(db.Document):
    """
    Publisher class

    The entity managing and distributing the comics
    Publishers may be an individual, author itself or a corporation
    """
    _id = db.ObjectIdField()
    name = db.StringField(max_length=200, required=True, unique=True)
    country = db.StringField(max_length=100, required=True)
    history = db.StringField(required=False)

    def to_dict(self) -> dict:
        return {
            "id": str(self._id),
            "name": self.name,
            "country": self.country,
            "history": self.history
        }
