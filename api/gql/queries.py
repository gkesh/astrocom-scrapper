from ariadne import ObjectType
from api.models.author import Author
from api.models.publisher import Publisher
from api.models.comic import Comic, ComicType


query = ObjectType("Query")


@query.field("authors")
def resolve_authors(*_) -> dict:
    try:
        authors = [author.to_dict() for author in Author.objects.all()]
        payload = {
            "status": True,
            "data": authors
        }
    except Exception as error:
        payload = {
            "status": False,
            "error": [str(error)]
        }
    return payload


@query.field("publishers")
def resolve_publishers(*_) -> dict:
    try:
        publishers = [publisher.to_dict() for publisher in Publisher.objects.all()]
        payload = {
            "status": True,
            "data": publishers
        }
    except Exception as error:
        payload = {
            "status": False,
            "error": [str(error)]
        }
    return payload


@query.field("comics")
def resolve_comics(*_) -> dict:
    try:
        comics = [comic.to_dict() for comic in Comic.objects.all()]
        payload = {
            "status": True,
            "data": comics
        }
    except Exception as error:
        payload = {
            "status": False,
            "error": [str(error)]
        }
    return payload


@query.field("titles")
def resolve_comic_titles(*_) -> dict:
    try:
        titles: list[dict[str, str]] = [{"title": title, "code": code} for code, title in Comic.objects.scalar('code', 'title')]
        payload = {
            "status": True,
            "data": titles
        }
    except Exception as error:
        payload = {
            "status": False,
            "error": [str(error)]
        }
    return payload


@query.field("types")
def resolve_comic_types(*_) -> dict:
    try:
        types: list[ComicType] = [item for item in list(ComicType)] 
        payload = {
            "status": True,
            "data": types
        }
    except Exception as error:
        payload = {
            "status": False,
            "error": [str(error)]
        }
    return payload


@query.field("comic")
def resolve_comic_chapters(*_, comic) -> dict:
    try:
        comic: Comic = Comic.objects.get(code=comic)
        payload = {
            "status": True,
            "data": comic.to_dict()
        }
    except Exception as error:
        payload = {
            "status": False,
            "error": [str(error)]
        }
    return payload


@query.field("chapters")
def resolve_comic_chapters(*_) -> dict:
    try:
        chapters: list[dict] = [{"code": comic.code, "count": comic.chapters.count()} for comic in Comic.objects]
        payload = {
            "status": True,
            "data": chapters
        }
    except Exception as error:
        payload = {
            "status": False,
            "error": [str(error)]
        }
    return payload


@query.field("chapter")
def resolve_comic_chapter(*_, comic, number) -> dict:
    try:
        chapters = Comic.objects.get(code=comic).chapters
        chapter: dict = chapters.get(number=number).to_dict()
        count: int = chapters.count()
        chapter["max"] = count

        payload = {
            "status": True,
            "data": chapter
        }
    except Exception as error:
        payload = {
            "status": False,
            "error": [str(error)]
        }
    return payload


def resolve_check_source(*_, url) -> bool:
    pass