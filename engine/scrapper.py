"""
Driver contains all the functions that can be used
by the api to fulfill the requests of the user
vis-a-vis the addition, removal, update, etc. of
comics.

Also includes experimental multi-threaded
download option.

@author gkesh
"""
from typing import Any
from bs4 import BeautifulSoup
from urllib.error import URLError
from urllib.request import Request, urlopen


class ScrapperError(Exception):
    pass


def fetch(link) -> tuple(bool, Any):
    try:
        page = urlopen(
            Request(
                link, 
                headers={'User-Agent': 'Mozilla/5.0'}
            )
        ).read().decode('utf-8')

        return True, page
    except URLError:
        # TODO: Implement Logging
        print("[Error] Invalid URL, Failed to fetch page.")
        return False, None


def soupify(scrapper):
    def inner(*args, **kwargs):
        status, page = fetch(kwargs['link'])
        soup = BeautifulSoup(page, 'html.parser') if status else None
        return scrapper(*args, soup=soup)
    return inner


@soupify
def scrape(crawler, **kwargs) -> list(str):
    if not kwargs['soup']:
        raise ScrapperError("Failed to pull page from link")
    return crawler(kwargs['soup'])
