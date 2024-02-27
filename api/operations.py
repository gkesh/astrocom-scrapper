from api.models.author import Author
from api.models.publisher import Publisher
from api.models.comic import (
    Genre,
    Comic,
    Chapter
)
from api import NAME
from logger.workers import info


def author_get_or_create(first_name, last_name) -> Author:
    """
    Creating Author

    Author object includes of two required fields: first_name & last_name
    & an optional field: biography
    """
    try:
        author = Author.objects.get(first_name=first_name, last_name=last_name)
    except Exception:
        info(NAME, f"Author {first_name} {last_name} not found, so creating...")
        author = Author(
            first_name=first_name, 
            last_name=last_name
        )
    author.save()
    return author

def publisher_get_or_create(name, country) -> Publisher:
    """
    Creating Publisher

    Publisher is an optional field in comics and may
    be omitted if not known or if sources are anonymous
    """
    try:
        publisher = Publisher.objects.get(name=name)
    except Exception:
        info(NAME, f"Publisher {name} not found, so creating...")
        publisher = Publisher(
            name=name, 
            country=country
        )
    publisher.save()
    return publisher


def genre_get_or_create(name) -> Genre:
    """
    Creating Genres

    Generally, a comic belongs to multiple genres and so
    a list of genres is supplied to the comic object

    Creating a list of Genre instances to add to the comics
    from a dictionary
    """
    try:
        genre = Genre.objects.get(name=name)
    except Exception:
        info(NAME, f"Genre {name} not found, so creating...")
        genre = Genre(
            name=name, 
            description=name
        )
    genre.save()
    return genre


def save_comic(comic: dict):
    """
    Creating Comics

    Needs multiple chapters and need to created iteratively 
    rest can be done easily with manual entry for now
    """

    chapter_docs = []

    if "chapters" in comic and comic["chapters"] is not None:
        chapter_docs = [Chapter(number=float(n+1), pages=p) for n, p in enumerate(comic.chapters)]

    comic_to_save = Comic(
        title=comic["title"],
        type=comic["type"],
        code=comic["code"],
        chapters=chapter_docs,
        synopsis=comic["synopsis"],
        source=comic["source"],
        crawler=comic["crawler"],
        date_published=comic["date_published"],
        ongoing=comic["ongoing"]
    )

    # Adding Genres
    [comic_to_save.genres.append(genre_get_or_create(genre["name"]).to_dbref()) for genre in comic["genres"]]
    
    # Adding author
    comic_to_save.author = author_get_or_create(comic["author"]["first_name"], comic["author"]["last_name"]).to_dbref()

    # Adding Publisher
    if "publisher" in comic and comic["publisher"] is not None:
        comic_to_save.publisher = publisher_get_or_create(comic["publisher"]["name"], comic["publisher"]["country"]).to_dbref()

    comic_saved = comic_to_save.save()
    return comic_saved
