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

from engine import NAME
from logger.workers import error


def save(image: Image, path: str) -> None:
    try:
        image.save(path)
    except OSError:
        error(NAME, "Failed to save image, attempting conversion...")
        image.convert('RGB').save(path)


def write(index: int, chapter: float, link: str, path: str) -> None:
    max_retries = int(env('MAX_RETRIES'))
    retries = max_retries

    while True:
        try:
            image = Image.open(BytesIO(get(link).content))
            path = f"{path}/chapter_{chapter}_{str(index)}.jpg"
            save(image, path)
            break
        except SSLError:
            error(NAME, f"SSL Error - Retrying download...[{max_retries - retries + 1}/{max_retries}]")
            if retries == 0: break
            retries = retries - 1
