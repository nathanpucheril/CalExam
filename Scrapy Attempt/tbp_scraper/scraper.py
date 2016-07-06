import scrapy
from scrapy.crawler import CrawlerProcess

from tbp_scraper.spiders.spider import tbp_scraper

process = CrawlerProcess({
    'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
})

process.crawl(tbp_scraper)
process.start() # the script will block here until the crawling is finished
