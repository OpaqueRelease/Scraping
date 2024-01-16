from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

from toscrape.spiders.scrapping_spider import BooksSpider


process = CrawlerProcess(get_project_settings())
process.crawl(BooksSpider)
process.start()