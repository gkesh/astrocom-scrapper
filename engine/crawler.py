"""
Crawlers go through the page and find the image
and create an array of links to the image.

Currently, there are two crawlers in written,
one is for kissmanga and one is a custom crawler
written to get the kaiju8 manga from the kaiju8
site.

@author gkesh
"""
kissmanga_crawler = lambda soup : [img["src"] for img in soup.find("div", {"id" : "centerDivVideo"}).findAll("img", recursive = False)]
kaiju_crawler = lambda soup : [img["src"] for img in soup.find("div", {"class": "entry-content"}).findAll("img", recursive = True)]

crawlers = {
    'kissmanga': kissmanga_crawler,
    'kaiju8': kaiju_crawler
}
