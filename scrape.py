from dotenv import load_dotenv
load_dotenv()

from engine import download

comic = "tales"
source = "https://kissmanga.org/chapter/manga-ax951880/"
roof = 5
floor = 1

download(comic, source, roof, floor=floor)