"""
Crawlers go through the page and find the image
and create an array of links to the image.

Currently, there are two crawlers in written,
one is for kissmanga and one is a custom crawler
written to get the kaiju8 manga from the kaiju8
site.

@author gkesh

Legacy Code:
kissmanga_crawler = lambda soup : [img["src"] for img in soup.find("div", {"id" : "centerDivVideo"}).findAll("img", recursive = False)]
kaiju_crawler = lambda soup : [img["src"] for img in soup.find("div", {"class": "entry-content"}).findAll("img", recursive = True)]

crawlers = {
    'kissmanga': kissmanga_crawler,
    'kaiju8': kaiju_crawler
}
"""
from abc import ABC, abstractmethod
from typing import List


class CrawlerException(Exception):
    pass


class Crawler(ABC):
    def __init__(self, soup) -> None:
        super().__init__()
        self.soup = soup

    @abstractmethod
    def collect(self) -> List[str]:
        pass

    @abstractmethod
    def crawl(self) -> List[str]:
        pass


class KissmangaCrawler(Crawler):
    def __init__(self, soup) -> None:
        super().__init__(soup)

    def collect(self) -> List[str]:
        return None
    
    def crawl(self) -> List[str]:
        return [img["src"] for img in self.soup.find("div", {"id" : "centerDivVideo"}).findAll("img", recursive = False)]


class KaijuCrawler(Crawler):
    def __init__(self, soup) -> None:
        super().__init__(soup)
    
    def collect(self) -> List[str]:
        return None

    def crawl(self) -> List[str]:
        return [img["src"] for img in self.soup.find("div", {"class": "entry-content"}).findAll("img", recursive = True)]


class CrawlerFactory:
    crawlers = {
        "kissmanga": KissmangaCrawler,
        "kaiju8": KaijuCrawler
    }

    @staticmethod
    def getCrawlers() -> List[str]:
        return CrawlerFactory.crawlers.keys()

    @staticmethod
    def createCrawler(name, soup) -> Crawler:
        if name not in CrawlerFactory.crawlers.keys():
            raise CrawlerException("Invalid crawler name, please select thr right crawler!")

        return CrawlerFactory.crawlers[name](soup)
