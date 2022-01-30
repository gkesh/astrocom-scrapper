from dotenv import load_dotenv
load_dotenv()

from api.models.author import Author
from api.models.publisher import Publisher
from api.models.comic import (
    Comic,
    ComicType,
    Genre,
    Chapter
)


print_process = lambda process: print(f"[INFO] Creating dummy {process}")

print_process("Author")
author = Author(
    first_name="Oda", 
    last_name="Eiichiro", 
    biography="Popular author in Shonen Jump hailing from the Saitama prefecture of Japan"
)
author.save()
print(author.to_dict())

print_process("Publisher")
publisher = Publisher(
    name="Jump Comics", 
    country="Japan", 
    history="Jump (ジャンプ, Janpu), sometimes stylized JUMP and also known as Jump Comics, is a line of manga anthologies (manga magazines) created by Shueisha. It began with Shōnen Jump manga anthology in 1968, later renamed Weekly Shōnen Jump. The origin of the name is unknown. The Jump anthologies are primarily intended for teen male audiences, although the Weekly Shōnen Jump magazine has also been popular with the female demographic. Along with the line of manga anthologies, Shōnen Jump also includes a crossover media franchise, where there have been various Shōnen Jump themed crossover anime and video games (since Famicom Jump) which bring together various Shōnen Jump manga characters."
)
publisher.save()
print(publisher.to_dict())

print_process("Comic")
genre = Genre(name="Action", description="Packed with fight scenes and massive power battles & world ending stakes. The battle of good and evil of epic proportions.")
chapter = Chapter(number=1, pages=20)
comic = Comic(
    title="One Piece",
    type=ComicType.MANGA,
    genres=[genre],
    chapters=[chapter],
    synopsis="The story follows the adventures of Monkey D. Luffy, a boy whose body gained the properties of rubber after unintentionally eating a Devil Fruit. With his pirate crew, the Straw Hat Pirates, Luffy explores the Grand Line in search of the world's ultimate treasure known as the One Piece in order to become the next King of the Pirates."
)

comic.author = author.to_dbref()
comic.publisher = publisher.to_dbref()
comic.save()
print(comic.to_dict())