from dotenv import load_dotenv
load_dotenv()

from engine import start

comic = "tales"
source = "https://kissmanga.org/chapter/manga-ax951880/"
roof = 362
floor = 360

start(comic, source, roof, floor=floor)