import scrapy


class GoogleScraperSpider(scrapy.Spider):
    name = "google_scraper"
    allowed_domains = ["google.com"]
    start_urls = ["https://google.com"]

    def parse(self, response):
        pass
