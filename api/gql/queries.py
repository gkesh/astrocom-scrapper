from ariadne import ObjectType
from api.models.author import Author
from api.models.publisher import Publisher
from api.models.comic import Comic
from api.models.comic import Chapter


query = ObjectType("Query")


@query.field("authors")
async def resolve_authors(*_) -> dict:
    try:
        result = await Author.objects.all()
        authors = [author.to_dict() for author in result]
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
async def resolve_publishers(*_) -> dict:
    try:
        result = await Publisher.objects.all()
        publishers = [publisher.to_dict() for publisher in result]
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
async def resolve_comics(*_) -> dict:
    try:
        result = await Comic.objects.all()
        comics = [comic.to_dict() for comic in result]
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
async def resolve_comic_titles(*_) -> dict:
    try:
        result = await Comic.objects.scalar('code', 'title')
        titles: list[dict[str, str]] = [{"title": title, "code": code} for code, title in result]
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


@query.field("comic")
async def resolve_comic_chapters(*_, comic) -> dict:
    try:
        comic: Comic = await Comic.objects.get(code=comic)
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
async def resolve_comic_chapters(*_) -> dict:
    try:
        result = await Comic.objects
        chapters: list[dict] = [{"code": comic.code, "count": comic.chapters.count()} for comic in result]
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
async def resolve_comic_chapter(*_, comic, number) -> dict:
    try:
        chapters = await Comic.objects.get(code=comic).chapters
        chapter: dict = await chapters.get(number=number).to_dict()
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