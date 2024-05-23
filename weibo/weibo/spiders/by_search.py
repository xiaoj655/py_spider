import scrapy


class BySerachSpider(scrapy.Spider):
    name = "by-search"
    allowed_domains = ["s.weibo.com"]
    start_urls = ["https://s.weibo.com"]

    def parse(self, response):
        print(response.text)
