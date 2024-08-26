from typing import List, Dict
from os import path, makedirs, getenv as env
from engine.scrapper import scrape
from engine.saver import write
from engine import NAME
from exceptions import ScrapperException, CrawlerException
from logger.workers import error, info, warn


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

@returns list(Chapter)
"""
def peek(source, crawler) -> List[Dict]:
    retries = int(env('MAX_RETRIES'))
    while retries > 0:
        try:
            chapters = scrape(crawler, link=source).collect()
            info(NAME, f"Discovered {len(chapters)} chapters")

            return chapters
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
@param floor: float - Start download from

@returns None
"""
def download(comic, source, crawler) -> None:
    retries = int(env('MAX_RETRIES'))
    scrapper = scrape(crawler, link=source)
    chapters = scrapper.collect()

    for chapter in chapters:
        info(NAME, f"Fetching chapter: {chapter['title'].strip()}")
        chapter_number = chapter['number']

        try:
            # Scrapping to get links for images
            images = scrape(crawler, link=chapter['source']).crawl()

            for index, image in enumerate(images):
                storage = path.join(env('OUT_DIR'), f"{comic}/chapter_{chapter_number}")
                if not path.isdir(storage): makedirs(storage)

                # Writing images
                write(index, chapter_number, image, storage)
                
            info(NAME, f"Wrote Chapter:: {chapter}")
        except ScrapperException:
            # Chapter test failed, Skipping...
            error(NAME, f"Failed to scrape chapter: {chapter_number}")
        except CrawlerException:
            error(NAME, "Crawler not found, exiting...")
            break
        except Exception:
            warn(NAME, f"Error while fetching chapter {chapter_number}, Retrying [{6 - retries} / 5]...")
            if retries == 0: break
            retries = retries - 1
