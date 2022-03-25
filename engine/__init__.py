"""
This is where the engine starts, i.e.
any code that wishes to run the scrapper
(Comic Downloader), has to start here.

This portion of the code will only be 
responsible for downloading the files
from the given link to the output folder.
Engine will act as an atomic unit and
will return status and nothing more!

NO DATABASE OPERATIONS HERE!! 

@author gkesh
"""
from os import path, makedirs, getenv as env
from engine.scrapper import scrape, ScrapperError
from engine.crawler import crawlers
from engine.saver import write


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
def peek(comic, source, external=False) -> list(float):
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
def download(comic, source, roof, external=False, floor = 0.0) -> None:
    retries = int(env('MAX_RETRIES'))
    while floor <= roof:
        try:
            chapter = "{:.1f}".format(floor).replace('.0', '')
            crawler = crawlers['kissmanga'] if not external else crawlers[comic]

            # Scrapping to get links for images
            images = scrape(crawler, link=f"{source}chapter-{chapter}")

            storage = path.join(env('OUT_DIR'), f"{comic}/chapter_{chapter}")
            if not path.isdir(storage): makedirs(storage)

            # Writing images
            for index, image in enumerate(images):
                write(index, chapter, image, storage)
            
            print(f"Wrote Chapter:: {chapter}")

            floor = floor + 0.1
        except ScrapperError:
            # Chapter test failed, Skipping...
            floor = floor + 0.1
        except KeyError:
            # TODO: Implement logging
            print("Crawler not found, exiting...")
            break
        except Exception:
            if retries == 0: break
            retries = retries - 1
