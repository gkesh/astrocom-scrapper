kissmanga_crawler = lambda soup : [img["src"] for img in soup.find("div", {"id" : "centerDivVideo"}).findAll("img", recursive = False)]
kaiju_crawler = lambda soup : [img["src"] for img in soup.find("div", {"class": "entry-content"}).findAll("img", recursive = True)]

crawlers = {
    'kissmanga': kissmanga_crawler,
    'kaiju8': kaiju_crawler
}
