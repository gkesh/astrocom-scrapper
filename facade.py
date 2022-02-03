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


print_process = lambda process: print(f"[INFO] Creating dummy {process}")

"""
Creating Author

Author object includes of two required fields: first_name & last_name
& an optional field: biography
"""

print_process("Author")

author = Author(
    first_name="Sung-Lak", 
    last_name="Jang"
)
author.save()

print(author.to_dict())

"""
Creating Publisher

Publisher is an optional field in comics and may
be omitted if not known or if sources are anonymous
"""

# print_process("Publisher")
# publisher = Publisher(
#     name="Jump Comics", 
#     country="Japan", 
#     history="Jump (ジャンプ, Janpu), sometimes stylized JUMP and also known as Jump Comics, is a line of manga anthologies (manga magazines) created by Shueisha. It began with Shōnen Jump manga anthology in 1968, later renamed Weekly Shōnen Jump. The origin of the name is unknown. The Jump anthologies are primarily intended for teen male audiences, although the Weekly Shōnen Jump magazine has also been popular with the female demographic. Along with the line of manga anthologies, Shōnen Jump also includes a crossover media franchise, where there have been various Shōnen Jump themed crossover anime and video games (since Famicom Jump) which bring together various Shōnen Jump manga characters."
# )
# publisher.save()
# print(publisher.to_dict())

"""
Creating Genres

Generally, a comic belongs to multiple genres and so
a list of genres is supplied to the comic object

Creating a list of Genre instances to add to the comics
from a dictionary
"""

print_process("Genres")

genres = [
    ["Action", "Action"],
    ["Adventure", "Adventure"],
    ["Shounen", "Shounen"],
    ["Fantasy", "Fantasy"]
]

genre_documents = []

for name, description in genres:
    genre = Genre(
        name=name, 
        description=description
    )
    genre.save()
    genre_documents.append(genre)


"""
Creating Comics

Needs multiple chapters and need to created iteratively 
rest can be done easily with manual entry for now
"""

print_process("Comic")

chapters = [28, 25, 35, 35, 34, 39, 47, 47, 37, 44, 46, 36, 46, 37, 46, 54, 49, 42, 42, 39, 41, 50, 44, 52, 38, 37, 48, 45, 45, 47, 40, 39, 48, 57, 44, 43, 46, 53, 53, 39, 45, 44, 41, 41, 56, 32, 37, 34, 40, 54, 60, 47, 57, 16, 37, 44, 36, 36, 31, 57, 44, 48, 51, 52, 59, 51, 56, 54, 70, 57, 59, 63, 61, 51, 50, 19, 47, 52, 49, 51, 47, 48, 49, 54, 55, 52, 59, 52, 46, 26, 103, 31, 25, 166, 45, 119, 121, 128, 38, 164, 119, 125, 182, 126, 154, 49, 55, 52, 45, 56, 11, 11, 7, 6, 7, 6, 42, 7, 8, 12, 14, 15, 51, 9, 6, 9, 7, 9, 89, 69, 69, 59, 48, 16, 16, 19, 16, 17, 18, 15, 16, 19, 16, 54, 56, 6, 67, 54, 75, 16, 67, 48, 50, 54, 47, 8, 60, 39, 44, 62, 65, 55, 9, 8, 9, 56, 55, 62, 90, 60, 59, 61, 54, 67]
chapter_documents = [Chapter(number=n, pages=p) for n, p in enumerate(chapters)]

comic = Comic(
    title="Solo Levelling",
    type=ComicType.MANHUA,
    code="solo",
    chapters=chapter_documents,
    synopsis="10 years ago, after `The Gate` that connected the real world with the monster world opened, some of the ordinary, everyday people received the power to hunt monsters within the Gate. They are known as `Hunters`. However, not all Hunters are powerful. My name is Sung Jin-Woo, an E-rank Hunter. I'm someone who has to risk his life in the lowliest of dungeons, the `World's Weakest`. Having no skills whatsoever to display, I barely earned the required money by fighting in low-leveled dungeons… at least until I found a hidden dungeon with the hardest difficulty within the D-rank dungeons! In the end, as I was accepting death, I suddenly received a strange power, a quest log that only I could see, a secret to leveling up that only I know about! If I trained in accordance with my quests and hunted monsters, my level would rise. Changing from the weakest Hunter to the strongest S-rank Hunter!"
)

[comic.genres.append(genre.to_dbref()) for genre in genre_documents]
comic.author = author.to_dbref()
# comic.publisher = publisher.to_dbref()
comic.save()
print(comic.to_dict())