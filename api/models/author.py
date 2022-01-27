from api import db


class Author(db.Document):
    """
    Author Class
    """
    first_name = db.StringField(max_length=200, required=True)
    last_name = db.StringField(max_length=200, required=True)
    biography = db.StringField(required=False)

    def to_dict(self) -> dict:
        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "biography": self.biography
        }