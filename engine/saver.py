"""
Saver module provides functions that save 
the files pulled from the link as images 
to the output directory stored in the 
evironment.

@author gkesh
"""
from os import getenv as env
from ssl import SSLError
from PIL import Image
from io import BytesIO
from requests import get
from requests.exceptions import SSLError


def save(image: Image, path: str) -> None:
    try:
        image.save(path)
    except OSError:
        image.convert('RGB').save(path)


def write(index: int, chapter: float, link: str, path: str) -> None:
    retries = int(env('MAX_RETRIES'))
    while True:
        try:
            image = Image.open(BytesIO(get(link).content))
            path = f"{path}/chapter_{chapter}_{str(index)}.jpg"
            save(image, path)
            break
        except SSLError:
            if retries == 0: break
            retries = retries - 1
