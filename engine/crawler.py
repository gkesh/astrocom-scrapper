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
from datetime import datetime
from typing import List

from exceptions import CrawlerException


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
        chapter_list = [li for li in self.soup.find("ul", {"class": "version-chap"}).findAll("li", recursive = False)]
        chapters = []

        for idx, chapter in enumerate(chapter_list):
            link = chapter.find("a")
            date_released = datetime.strptime(chapter.find("span", {"class": "chapter-release-date"}).find("i").text, "%B %d, %Y").date() if idx == len(chapter_list) - 1 else datetime.now()
            
            source = link["href"]
            title = link.text
            number = float(title.split(" ")[1])

            chapters.append({
                "number": number,
                "title": title,
                "date_released": date_released,
                "source": source,
                "pages": 0
            })

        return chapters
    
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
