from typing import Dict, List
from ariadne import QueryType
from api.gql import responder
from api.models.author import Author
from api.models.publisher import Publisher
from api.models.comic import Comic, ComicType
from engine.crawler import CrawlerFactory


query = QueryType()


@query.field("authors")
@responder(Exception)
def resolve_authors(*_) -> List[Dict]:
    return [author.to_dict() for author in Author.objects.all()]


@query.field("publishers")
@responder(Exception)
def resolve_publishers(*_) -> List[Dict]:
    return [publisher.to_dict() for publisher in Publisher.objects.all()]


@query.field("comics")
@responder(Exception)
def resolve_comics(*_) -> List[Dict]:
    return [comic.to_dict() for comic in Comic.objects.all()]


@query.field("titles")
@responder(Exception)
def resolve_comic_titles(*_) -> List[Dict[str, str]]:
    return [{"title": title, "code": code} for code, title in Comic.objects.scalar('code', 'title')]


@query.field("selects")
@responder(Exception)
def resolve_comic_types(*_) -> Dict:
    types: list[ComicType] = [item for item in list(ComicType)] 
    crawlers: list[str] = CrawlerFactory.crawlers

    return {
        "types": types,
        "crawlers": crawlers
    }


@query.field("comic")
@responder(Exception)
def resolve_comic_chapters(*_, comic) -> Comic:
    return Comic.objects.get(code=comic).to_dict()


@query.field("chapters")
@responder(Exception)
def resolve_comic_chapters(*_) -> List[Dict]:
    return [{"code": comic.code, "count": comic.chapters.count()} for comic in Comic.objects]


@query.field("chapter")
@responder(Exception)
def resolve_comic_chapter(*_, comic, number) -> dict:
    chapters = Comic.objects.get(code=comic).chapters
    chapter: dict = chapters.get(number=number).to_dict()
    count: int = chapters.count()
    chapter["max"] = count

    return chapter


def resolve_check_source(*_, url) -> bool:
    pass
