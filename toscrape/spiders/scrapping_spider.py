
from pathlib import Path

import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.spiders import CrawlSpider
from scrapy import cmdline

from scrapy.item import Item, Field
class ToscrapeItem(scrapy.Item):
    title = Field()
    url = Field()

class BooksSpider(scrapy.Spider):
    name = "books"
    # allowed_domains = "books.toscrape.com"
    custom_settings = {
                       'CLOSESPIDER_ITEMCOUNT': 500,
                       }
    
    def start_requests(self):
        urls = [
            "https://books.toscrape.com/",
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        books = response.css('article.product_pod')
        for book in books:
            item = ToscrapeItem()
            item["title"] = book.css('h3 a::text').get()
            item["url"] = book.css('img').attrib['src']
            yield item

        next_page = response.css('li.next a ::attr(href)').get()
        if next_page is not None:
            if 'catalogue/' in next_page:
                next_page_url = 'https://books.toscrape.com/' + next_page
            else:
                next_page_url = 'https://books.toscrape.com/catalogue/' + next_page
            yield response.follow(next_page_url, callback=self.parse)