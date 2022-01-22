from models.author import Author


def resolve_authors(obj, info):
    try:
        authors = [author.to_dict() for author in Author.objects.all()]
        payload = {
            "success": True,
            "authors": authors
        }
    except Exception as error:
        payload = {
            "success": False,
            "error": [str(error)]
        }
    return payload