"""
Driver contains all the functions that can be used
by the api to fulfill the requests of the user
vis-a-vis the addition, removal, update, etc. of
comics.

Also includes experimental multi-threaded
download option.

@author gkesh
"""
from bs4 import BeautifulSoup
from urllib.error import URLError
from urllib.request import Request, urlopen


class ScrapperError(Exception):
    pass


def soupify(scrapper):
    def inner(*args, **kwargs):
        try:
            soup = BeautifulSoup(
                urlopen(
                    Request(
                        kwargs['link'], 
                        headers={'User-Agent': 'Mozilla/5.0'}
                    )
                ).read().decode('utf-8'), 
                'html.parser'
            )
        except URLError:
            soup = None
        return scrapper(*args, soup=soup)
    return inner


@soupify
def scrape(crawler, **kwargs):
    if not kwargs['soup']:
        raise ScrapperError("Failed to pull page from link")
    return crawler(kwargs['soup'])
