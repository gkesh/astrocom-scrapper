from api.models.author import Author
from api.models.publisher import Publisher


def resolve_authors(obj, info) -> dict:
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


def resolve_publishers(obj, info) -> dict:
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