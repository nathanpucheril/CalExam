from Core import HknScraper, TbpScraper
from itertools import chain



SCRAPERS = [TbpScraper, HknScraper]

def scrape():
    return chain.from_iterable([scraper.scrape() for scraper in SCRAPERS])
