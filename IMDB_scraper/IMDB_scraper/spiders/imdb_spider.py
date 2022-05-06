# to run GITHUB
# scrapy crawl imdb_spider -o movies.csv

import scrapy
from scrapy.http import Request

class ImdbSpider(scrapy.Spider):
    name = 'imdb_spider'
    
    start_urls = ['https://www.imdb.com/title/tt0898266/']

    def parse(self, response):
        new_url = response.url + "fullcredits"
        yield Request(new_url, callback = self.parse_full_credits)
    
    def parse_full_credits(self, response):
        for i in [a.attrib["href"] for a in response.css("td.primary_photo a")]:
            new_url = response.urljoin(i)
            yield Request(new_url, callback = self.parse_actor_page)
            
    def parse_actor_page(self, response):
        actor = response.css("div.name-overview-widget h1.header span.itemprop::text").get()
        for element in response.css("div.filmo-row"):
            movietv = element.css("div.filmo-row b a::text").get()
            yield {
                "actor" : actor, 
                "movie_or_TV_name" : movietv
            }
