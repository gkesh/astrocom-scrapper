from dotenv import load_dotenv
load_dotenv()

from engine import download

comic = "tales"
source = "https://kissmanga.org/chapter/manga-ax951880/"
roof = 366
floor = 363

download(comic, source, roof, floor=floor)