from api import db
from enum import IntEnum
from api.models.author import Author
from api.models.publisher import Publisher
from api.models.genre import Genre
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
    number = db.FloatField(min_value=0.0, required=True)
    title = db.StringField(max_length=200, required=False)
    pages = db.IntField(min_value=0)
    visited = db.BooleanField()
    checkpoint = db.BooleanField()
    date_released = db.DateTimeField(required=True, default=datetime.utcnow)

    def to_dict(self) -> dict:
        return {
            "number": self.number,
            "title": self.title,
            "pages": self.pages,
            "visited": True if self.visited is not None else False,
            "checkpoint": True if self.checkpoint is not None else False,
            "date_released": str(self.date_released.strftime('%d-%m-%Y'))
        }


class Comic(db.Document):
    """
    Comic Class

    Any type of visually readable graphic depiction of story.
    Encompases western comics, manga, manhwa, manhua, web novels, etc.
    """
    _id = db.ObjectIdField()
    title = db.StringField(max_length=200, required=True)
    code = db.StringField(max_length=20, required=True, unique=True)
    source = db.URLField(required=True, unique=True)
    crawler = db.StringField(max_lenth=20, required=True)
    type = db.EnumField(ComicType, default=ComicType.MANGA)
    genres = db.ListField(db.ReferenceField(Genre, dbref=True, reverse_delete_rule=1), default=[])
    chapters = db.EmbeddedDocumentListField(Chapter)
    ongoing = db.BooleanField()
    author = db.ReferenceField(Author, dbref=True, required=True, reverse_delete_rule=3)
    publisher = db.ReferenceField(Publisher, dbref=True, reverse_delete_rule=1)
    synopsis = db.StringField(required=False)
    date_published = db.DateTimeField(required=True, default=datetime.utcnow)
    date_updated = db.DateTimeField(default=datetime.utcnow)

    def to_dict(self) -> dict:
        return {
            "id": str(self._id),
            "title": self.title,
            "code": self.code,
            "source": self.source,
            "crawler": self.crawler,
            "type": self.type,
            "genres": [genre.to_dict() for genre in self.select_related().genres],
            "chapters": [chapter.to_dict() for chapter in self.chapters],
            "ongoing": self.ongoing,
            "author": self.author.to_dict(),
            "publisher": self.publisher.to_dict() if self.publisher else {"name": "N/A"},
            "synopsis": self.synopsis,
            "date_published": str(self.date_published.strftime('%d-%m-%Y')),
            "date_updated": str(self.date_updated.strftime('%d-%m-%Y'))
        }

