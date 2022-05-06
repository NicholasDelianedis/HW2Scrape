# to run
# scrapy crawl imdb_spider -o movies.csv

import scrapy
from scrapy.http import Request

class ImdbSpider(scrapy.Spider):
    name = 'imdb_spider'
    
    start_urls = ['https://www.imdb.com/title/tt0898266/']

    def parse(self, response):
        """
        Directs scraper from movie/show page to its credits page
        """
        new_url = response.url + "fullcredits" # obtain credits page url
        yield Request(new_url, callback = self.parse_full_credits)
        # call parse_full_credits with new url
    
    def parse_full_credits(self, response):
        """
        Direct scraper to each actor on the credits page by calling the
        url from each actor's picture
        """
        for i in [a.attrib["href"] for a in response.css("td.primary_photo a")]:
            new_url = response.urljoin(i) # obtain actor's url page
            yield Request(new_url, callback = self.parse_actor_page)
            # call parse_actor_page on each actor's url page
            
    def parse_actor_page(self, response):
        """
        Scrape actor page by extracting actor name and movie or tv show
        name for each movie or tv show actor was involved in
        """
        actor = response.css("div.name-overview-widget h1.header span.itemprop::text").get()
        # use css selectors to get the actor's name
        for element in response.css("div.filmo-row"):
            movietv = element.css("div.filmo-row b a::text").get()
            # obtain movie/tv show name through css selectors
            yield {
                "actor" : actor, 
                "movie_or_TV_name" : movietv
            }
            # yield a dict with the actor name and movie/tv show name
