# to run GITHUB
# scrapy crawl imdb_spider -o movies.csv

import scrapy

class ImdbSpider(scrapy.Spider):
    name = 'imdb_spider'
    
    start_urls = ['https://www.imdb.com/title/tt0898266/']

    def parse(self, response):
        filename = f'imdb.html'
        with open(filename, 'wb') as f:
            f.write(response.body)

 #   def parse(self, response):
 #       new_url = response.url + "fullcredits"
 #       request = Request(new_url, callback = parse_full_credits)
 #       yield request
    
    def parse_full_credits(self, response):
        [a.attrib["href"] for a in response.css("td.primary_photo a")]
        Request(new_url, callback = parse_actor_page)

    def parse_actor_page(self, repsonse):
        element.css("::attr(id)")
        element.css("div.filmo-row")
        element.css("a::text")
