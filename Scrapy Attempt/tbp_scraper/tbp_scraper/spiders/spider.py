from scrapy import Spider
from scrapy.selector import Selector

from tbp_scraper.items import TbpScraperItem


class tbp_scraper(Spider):
    name = "tbp_scraper"
    allowed_domains = ["https://tbp.berkeley.edu"]
    start_urls = [
        "https://tbp.berkeley.edu/courses/cs/61A/",
    ]

    def parse(self, response):

        def exists(selector, xpath):
            return bool(int(selector.xpath("boolean(" + xpath +  ")").extract()[0]))

        def safe_assignment(selector, xpath, assignment_prefix=""):
            if exists(selector, xpath):
                return assignment_prefix + selector.xpath(xpath).extract()[0]
            else:
                return "n/a"

        row_xpath = "//*[@id='content']/table[1]/tbody/tr"

        table_rows = Selector(response).xpath(row_xpath)
        for row in table_rows:
            item = TbpScraperItem()
            item["professor"] = safe_assignment(row, "td[1]/a/text()")
            item["mt_type"] = safe_assignment(row, "td[2]/text()")
            item["year"] = safe_assignment(row, "td[3]/text()")

            # professor = Field()
            item["exam_url"] = safe_assignment(row, "td[4]/a/@href", self.allowed_domains[0])
            item["sol_url"] = safe_assignment(row, "td[4]/a/@href", self.allowed_domains[0])
            yield item
