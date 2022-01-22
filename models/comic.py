from email.policy import default
from pydoc import synopsis
from api import db
from enum import Enum, auto
from datetime import datetime


class ComicType(Enum):
    """
    Comic Type Enum

    Defines the type of the medium
    """
    MANGA = auto() # Japanese
    WESTERN = auto()
    MANHUA = auto() # Chinese
    MANHWA = auto() # Korean
    WEB = auto()


class Genre(db.EmbeddedDocument):
    """
    Genre Class

    The genre defines the category any creation
    belongs to and helps identify its nature
    """
    name = db.StringField(max_length=100, required=True)
    description = db.StringField(required=True)

    def to_dict(self) -> dict:
        return {
            "name": self.name,
            "description": self.description
        }


class Chapter(db.EmbeddedDocument):
    """
    Chapter Class

    Used to store information on the chapters
    which may include title, date released, 
    page count, etc.
    """
    title = db.StringField(max_length=200, required=False)
    pages = db.ListField(db.ImageField(thumbnail_size=(64, 100, True)))
    date_released = db.DateTimeField(required=True, default=datetime.utcnow)

    def to_dict(self) -> dict:
        return {
            "title": self.title,
            "pages": self.pages,
            "date_released": self.date_released
        }


class Comic(db.Document):
    """
    Comic Class

    Any type of visually readable graphic depiction of story.
    Encompases western comics, manga, manhwa, manhua, web novels, etc.
    """
    title = db.StringField(max_length=200, required=True)
    cover = db.ImageField(size=(320, 500, True), thumbnail_size=(64, 100, True), required=True)
    type = db.EnumField(ComicType, default=ComicType.MANGA)
    genres = db.ListField(db.EmbeddedDocumentField(Genre))
    chapters = db.ListField(db.EmbeddedDocumentField(Chapter))
    synopsis = db.StringField(required=False)
    date_published = db.DateTimeField(required=True, default=datetime.utcnow)
    date_updated = db.DateTimeField(default=datetime.utcnow)

    def to_dict(self) -> dict:
        return {
            "title": self.title,
            "type": self.type,
            "genres": [genre.to_dict() for genre in self.genres],
            "chapters": [chapter.to_dict() for chapter in self.chapters],
            "synopsis": self.synopsis,
            "date_published": self.date_published,
            "date_updated": self.date_updated
        }

