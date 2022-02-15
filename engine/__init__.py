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


def start(comic, source, roof, custom_crawler=False, floor = 0.0) -> None:
    retries = int(env('MAX_RETRIES'))
    while floor <= roof:
        try:
            chapter = "{:.1f}".format(floor).replace('.0', '')
            crawler = crawlers['kissmanga'] if not custom_crawler else crawlers[comic]

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
