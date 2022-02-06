from datetime import datetime
from dotenv import load_dotenv
load_dotenv()

from api.models.author import Author
from api.models.publisher import Publisher
from api.models.comic import (
    Genre,
    Comic,
    ComicType,
    Chapter
)


def author_get_or_create(first_name, last_name) -> Author:
    """
    Creating Author

    Author object includes of two required fields: first_name & last_name
    & an optional field: biography
    """
    try:
        author = Author.objects.get(first_name=first_name, last_name=last_name)
    except Exception:
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
        print(f"Publisher {name} not found, so creating...")
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
        print(f"Genre {name} not found, so creating...")
        genre = Genre(
            name=name, 
            description=name
        )
    genre.save()
    return genre


def save_facade(author_fn, author_ln, publisher_n, publisher_c, comic_n, comic_t, comic_c, comic_ch, comic_s, comic_g, comic_p, comic_o, comic_src):
    """
    Creating Comics

    Needs multiple chapters and need to created iteratively 
    rest can be done easily with manual entry for now
    """

    chapter_documents = [Chapter(number=n+1, pages=p) for n, p in enumerate(comic_ch)]

    comic = Comic(
        title=comic_n,
        type=comic_t,
        code=comic_c,
        chapters=chapter_documents,
        synopsis=comic_s,
        ongoing=comic_o,
        source=comic_src,
        date_published=comic_p
    )

    # Adding Genres
    [comic.genres.append(genre_get_or_create(genre).to_dbref()) for genre in comic_g]
    
    # Adding author
    comic.author = author_get_or_create(author_fn, author_ln).to_dbref()

    # Adding Publisher
    if publisher_n is not None and publisher_c is not None:
        comic.publisher = publisher_get_or_create(publisher_n, publisher_c).to_dbref()

    comic.save()
    print(comic.to_dict())


comic_facades = [
    {
        "title": "Solo Leveling",
        "chapters": [28, 25, 35, 35, 34, 39, 47, 47, 37, 44, 46, 36, 46, 37, 46, 54, 49, 42, 42, 39, 41, 50, 44, 52, 38, 37, 48, 45, 45, 47, 40, 39, 48, 57, 44, 43, 46, 53, 53, 39, 45, 44, 41, 41, 56, 32, 37, 34, 40, 54, 60, 47, 57, 16, 37, 44, 36, 36, 31, 57, 44, 48, 51, 52, 59, 51, 56, 54, 70, 57, 59, 63, 61, 51, 50, 19, 47, 52, 49, 51, 47, 48, 49, 54, 55, 52, 59, 52, 46, 26, 103, 31, 25, 166, 45, 119, 121, 128, 38, 164, 119, 125, 182, 126, 154, 49, 55, 52, 45, 56, 11, 11, 7, 6, 7, 6, 42, 7, 8, 12, 14, 15, 51, 9, 6, 9, 7, 9, 89, 69, 69, 59, 48, 16, 16, 19, 16, 17, 18, 15, 16, 19, 16, 54, 56, 6, 67, 54, 75, 16, 67, 48, 50, 54, 47, 8, 60, 39, 44, 62, 65, 55, 9, 8, 9, 56, 55, 62, 90, 60, 59, 61, 54, 67, 54, 13, 10, 5, 49],
        "synopsis": "10 years ago, after `The Gate` that connected the real world with the monster world opened, some of the ordinary, everyday people received the power to hunt monsters within the Gate. They are known as `Hunters`. However, not all Hunters are powerful. My name is Sung Jin-Woo, an E-rank Hunter. I'm someone who has to risk his life in the lowliest of dungeons, the `World's Weakest`. Having no skills whatsoever to display, I barely earned the required money by fighting in low-leveled dungeons… at least until I found a hidden dungeon with the hardest difficulty within the D-rank dungeons! In the end, as I was accepting death, I suddenly received a strange power, a quest log that only I could see, a secret to leveling up that only I know about! If I trained in accordance with my quests and hunted monsters, my level would rise. Changing from the weakest Hunter to the strongest S-rank Hunter!",
        "author": {
            "first_name": "Sung-Lak",
            "last_name": "Jang"
        },
        "publisher": {
            "name": "D&C Media", 
            "country": "Korea"
        },
        "code": "solo",
        "source": "https://kissmanga.org/chapter/manga-dr980474/",
        "type": ComicType.MANHWA,
        "genres": ["Action", "Adventure", "Shounen", "Fantasy"],
        "ongoing": False,
        "date_published": datetime(2016, 11, 4)
    },
    {
        "title": "Demon Slayer",
        "chapters": [54, 24, 22, 18, 18, 18, 20, 19, 18, 18, 18, 18, 18, 18, 18, 22, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 20, 18, 21, 21, 18, 18, 18, 19, 20, 18, 18, 20, 18, 18, 18, 18, 18, 21, 18, 21, 18, 21, 17, 18, 20, 19, 18, 18, 18, 20, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 22, 18, 18, 18, 20, 18, 18, 19, 18, 21, 18, 18, 18, 18, 18, 18, 18, 21, 18, 18, 18, 18, 18, 20, 18, 19, 18, 18, 20, 22, 17, 18, 18, 18, 18, 18, 17, 18, 20, 20, 18, 18, 21, 18, 18, 18, 18, 18, 20, 18, 18, 18, 21, 18, 22, 17, 18, 21, 18, 18, 18, 18, 16, 20, 19, 19, 18, 18, 18, 18, 19, 18, 20, 20, 19, 18, 19, 18, 18, 22, 18, 18, 17, 18, 18, 20, 18, 19, 17, 20, 20, 18, 23, 20, 20, 18, 20, 18, 17, 21, 18, 17, 18, 18, 18, 18, 17, 18, 20, 18, 26, 18, 18, 18, 17, 19, 18, 22, 18, 18, 19, 28],
        "synopsis": "Tanjiro is the oldest son in his family who has lost his father. One day, Tanjiro ventures off to another town to sell charcoal. Instead of going home, he ends up staying the night at someone else's house due to rumors of a demon nearby in the mountains. When he gets home the following day, a terrible tragedy awaits him.",
        "author": {
            "first_name": "Koyoharu",
            "last_name": "Gotouge"
        },
        "publisher": {
            "name": "Shueisha", 
            "country": "Japan"
        },
        "code": "kimetsu",
        "source": "https://kissmanga.org/manga/manga-to970571",
        "type": ComicType.MANGA,
        "genres": ["Historical", "Adventure", "Shounen", "Fantasy"],
        "ongoing": False,
        "date_published": datetime(2016, 2, 15)
    },
    {
        "title": "Omniscient Reader",
        "chapters": [13, 28, 37, 50, 5, 45, 41, 11, 7, 12, 9, 10, 8, 9, 32, 18, 25, 8, 22, 25, 73, 51, 39, 66, 55, 21, 33, 10, 10, 21, 25, 84, 32, 65, 42, 8, 73, 44, 43, 37, 46, 32, 102, 60, 26, 53, 18, 28, 54, 59, 54, 16, 61, 62, 15, 51, 26, 61, 55, 20, 113, 7, 9, 68, 8, 49, 71, 18, 6, 26, 59, 87, 83, 119, 159, 13, 121, 95, 83, 6, 7],
        "synopsis": "‘This is a development that I know of.’ The moment he thought that, the world had been destroyed, and a new universe had unfolded. The new life of an ordinary reader begins within the world of the novel, a novel that he alone had finished.",
        "author": {
            "first_name": "Sing",
            "last_name": "Shong"
        },
        "publisher": {
            "name": None, 
            "country": None
        },
        "code": "omniscient",
        "source": "https://kissmanga.org/chapter/manga-iw985579/",
        "type": ComicType.MANHWA,
        "genres": ["Action", "Adventure", "Isekai", "Fantasy"],
        "ongoing": True,
        "date_published": datetime(2020, 1, 1)
    },
    {
        "title": "Kaiju No. 8",
        "chapters": [51, 35, 22, 18, 15, 22, 18, 19, 15, 18, 18, 16, 19, 17, 16, 20, 17, 19, 14, 17, 18, 18, 15, 15, 20, 18, 18, 16, 18, 15, 15, 16, 20, 21, 16, 20, 17, 19, 22, 20, 21, 24, 18, 21, 26, 19, 19, 24, 15, 20, 18, 20, 16, 24, 3],
        "synopsis": "Grotesque, Godzilla-like monsters called “kaijuu” have been appearing around Japan for many years. To combat these beasts, an elite military unit known as the Defense Corps risks their lives daily to protect civilians. Once a creature is killed, “sweepers”—working under the Professional Kaijuu Cleaner Corporation—are left to dispose of its remains.",
        "author": {
            "first_name": "Naoya",
            "last_name": "Matsumoto"
        },
        "publisher": {
            "name": "Shueisha", 
            "country": "Japan"
        },
        "code": "kaiju8",
        "source": "https://kaijuno-8.com/manga/read-kaiju-no-8monster-8-",
        "type": ComicType.MANGA,
        "genres": ["Action", "Comedy", "Mecha"],
        "ongoing": True,
        "date_published": datetime(2020, 7, 3)
    }
]


for facade in comic_facades:
    save_facade(
        author_fn=facade["author"]["first_name"],
        author_ln=facade["author"]["last_name"],
        publisher_n=facade["publisher"]["name"],
        publisher_c=facade["publisher"]["country"],
        comic_n=facade["title"],
        comic_t=facade["type"],
        comic_c=facade["code"],
        comic_ch=facade["chapters"],
        comic_s=facade["synopsis"],
        comic_g=facade["genres"],
        comic_p=facade["date_published"],
        comic_o=facade["ongoing"],
        comic_src=facade["source"]
    )