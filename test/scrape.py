from dotenv import load_dotenv
load_dotenv()

from engine import download

comic = "tales"
source = "https://kissmanga.org/chapter/manga-ax951880/"
roof = 362
floor = 360

download(comic, source, roof, floor=floor)