from typing import Dict, List
from ariadne import QueryType
from api.gql import responder
from api.models.author import Author
from api.models.publisher import Publisher
from api.models.comic import Comic, ComicType
from engine.crawler import CrawlerFactory
from mongoengine import Q


query = QueryType()


@query.field("authors")
@responder()
def resolve_authors(*_) -> List[Dict]:
    return [author.to_dict() for author in Author.objects.all()]


@query.field("search_authors")
@responder()
def resolve_search_authors(*_, keyword: str) -> List[Dict]:
    return [author.to_dict() for author in Author.objects(
        Q(first_name__istartswith=keyword) | Q(last_name__istartswith=keyword)
    )]

@query.field("publishers")
@responder()
def resolve_publishers(*_) -> List[Dict]:
    return [publisher.to_dict() for publisher in Publisher.objects.all()]


@query.field("search_publishers")
@responder()
def resolve_search_publishers(*_, keyword: str) -> List[Dict]:
    return [publisher.to_dict() for publisher in Publisher.objects(name__istartswith=keyword)]


@query.field("comics")
@responder()
def resolve_comics(*_) -> List[Dict]:
    return [comic.to_dict() for comic in Comic.objects.all()]


@query.field("titles")
@responder()
def resolve_comic_titles(*_) -> List[Dict[str, str]]:
    return [{"title": title, "code": code} for code, title in Comic.objects.scalar('code', 'title')]


@query.field("selects")
@responder()
def resolve_comic_types(*_) -> Dict:
    types: list[ComicType] = [item for item in list(ComicType)] 
    crawlers: list[str] = CrawlerFactory.crawlers

    return {
        "types": types,
        "crawlers": crawlers
    }


@query.field("comic")
@responder()
def resolve_comic_chapters(*_, comic) -> Comic:
    return Comic.objects.get(code=comic).to_dict()


@query.field("chapters")
@responder()
def resolve_comic_chapters(*_) -> List[Dict]:
    return [{"code": comic.code, "count": comic.chapters.count()} for comic in Comic.objects]


@query.field("chapter")
@responder()
def resolve_comic_chapter(*_, comic, number) -> dict:
    chapters = Comic.objects.get(code=comic).chapters
    chapter: dict = chapters.get(number=number).to_dict()
    count: int = chapters.count()
    chapter["max"] = count

    return chapter

@query.field("download_chapters")
@responder
def resolve_download_chapter(*_, comic) -> bool:
    # TODO: Implement chapter list feature (check function)
    pass
