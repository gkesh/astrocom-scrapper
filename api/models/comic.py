from api import db
from api.models.author import Author
from api.models.publisher import Publisher
from api.models.genre import Genre
from enum import IntEnum
from datetime import datetime


class ComicType(IntEnum):
    """
    Comic Type Enum

    Defines the type of the medium
    """
    MANGA = 1 # Japanese
    WESTERN = 2
    MANHUA = 3 # Chinese
    MANHWA = 4 # Korean
    WEB = 5


class Chapter(db.EmbeddedDocument):
    """
    Chapter Class

    Used to store information on the chapters
    which may include title, date released, 
    page count, etc.
    """
    number = db.IntField(min_value=0, required=True)
    title = db.StringField(max_length=200, required=False)
    pages = db.IntField(min_value=0)
    date_released = db.DateTimeField(required=True, default=datetime.utcnow)

    def to_dict(self) -> dict:
        return {
            "number": self.number,
            "title": self.title,
            "pages": self.pages,
            "date_released": str(self.date_released.strftime('%d-%m-%Y'))
        }


class Comic(db.Document):
    """
    Comic Class

    Any type of visually readable graphic depiction of story.
    Encompases western comics, manga, manhwa, manhua, web novels, etc.
    """
    _id = db.ObjectIdField()
    title = db.StringField(max_length=200, required=True, unique=True)
    type = db.EnumField(ComicType, default=ComicType.MANGA)
    genres = db.ListField(db.ReferenceField(Genre))
    chapters = db.ListField(db.EmbeddedDocumentField(Chapter))
    author = db.ReferenceField(Author, required=True, reverse_delete_rule=3)
    publisher = db.ReferenceField(Publisher, reverse_delete_rule=1)
    synopsis = db.StringField(required=False)
    date_published = db.DateTimeField(required=True, default=datetime.utcnow)
    date_updated = db.DateTimeField(default=datetime.utcnow)

    def to_dict(self) -> dict:
        return {
            "id": str(self._id),
            "title": self.title,
            "type": self.type,
            "genres": [genre.to_dict() for genre in self.genres],
            "chapters": [chapter.to_dict() for chapter in self.chapters],
            "author": self.author.to_dict(),
            "publisher": self.publisher.to_dict(),
            "synopsis": self.synopsis,
            "date_published": str(self.date_published.strftime('%d-%m-%Y')),
            "date_updated": str(self.date_updated.strftime('%d-%m-%Y'))
        }

