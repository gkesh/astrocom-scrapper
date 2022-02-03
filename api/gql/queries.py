from ariadne import ObjectType
from api.models.author import Author
from api.models.publisher import Publisher
from api.models.comic import Comic


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
        titles = [{"title": title, "code": code} for code, title in Comic.objects.scalar('code', 'title')]
        payload = {
            "status": True,
            "data": titles
        }
    except Exception as error:
        payload = {
            "status": False,
            "data": [str(error)]
        }
    return payload

@query.field("chapters")
def resolve_comic_chapters(*_) -> dict:
    # TODO: Implement Chpaters Query based on Variable
    pass

@query.field("chapter")
def resolve_comic_chapter(*_) -> dict:
    # TODO: Implement specific chapter fetch
    pass