from typing import List
from os import path, makedirs, getenv as env
from engine.scrapper import scrape
from engine.saver import write
from engine import NAME
from exceptions import ScrapperException, CrawlerException
from logger.workers import error, info


"""
Check

Function to test whether a page link provided 
has chapters inside it. This proves the validity of
the page and lets us know that the link entered
by the user is a valid one.

@param source: str - Link to comic chapters page
@returns boolean
"""
def check(crawler, source) -> bool:
    chapters = scrape(crawler, link=source).collect()
    return chapters is not None


"""
Peek

Check which chapters exist and generate a 
list of chapters that exist for a specific 
comic.

@param comic: str - Code for the target comic
@param source: str - Chapters base link
@param external: bool - Download source not default

@returns list(float)
"""
def peek(comic, source, external=False) -> List[float]:
    retries = int(env('MAX_RETRIES'))
    while retries > 0:
        try:
            pass
        except Exception:
           retries = retries - 1


"""
Download

The download function crawls the chapter pages and
scrapes the links for the images. The scraped links
are then downloaded using the write function from
saver module.

@param comic: str - Code for the target comic
@param source: str - Chapters base link
@param roof: float - Stop download at
@param external: bool - Download source not default
@param floor: float - Start download from

@returns None
"""
def download(comic, source, roof, crawler="kissmanga", floor = 0.0) -> None:
    retries = int(env('MAX_RETRIES'))
    while floor <= roof:
        try:
            chapter = "{:.1f}".format(floor).replace('.0', '')

            # Scrapping to get links for images
            images = scrape(crawler, link=f"{source}chapter-{chapter}").crawl()

            storage = path.join(env('OUT_DIR'), f"{comic}/chapter_{chapter}")
            if not path.isdir(storage): makedirs(storage)

            # Writing images
            for index, image in enumerate(images):
                write(index, chapter, image, storage)
            
            info(NAME, f"Wrote Chapter:: {chapter}")

            floor = floor + 0.1
        except ScrapperException:
            # Chapter test failed, Skipping...
            floor = floor + 0.1
        except CrawlerException:
            error(NAME, "Crawler not found, exiting...")
            break
        except Exception:
            if retries == 0: break
            retries = retries - 1
