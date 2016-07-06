from scrapy import Spider
from scrapy.selector import Selector

from tbp_scraper.items import HKNScraperItem


class hkn_scraper(Spider):
    name = "hkn_scraper"
    allowed_domains = ["https://hkn.eecs.berkeley.edu"]
    start_urls = [
        "https://hkn.eecs.berkeley.edu/exams/course/cs/3",
    ]

    def parse(self, response):

        def exists(selector, xpath):
            return bool(int(selector.xpath("boolean(" + xpath +  ")").extract()[0]))

        def safe_assignment(selector, xpath, assignment_prefix=""):
            if exists(selector, xpath):
                return (assignment_prefix + selector.xpath(xpath).extract()[0]).strip()
            else:
                return None

        row_xpath = "//*[@id='exams']/tr"
        table_rows = Selector(response).xpath(row_xpath)
        exam_types = ["Midterm 1", "Midterm 2", "Midterm 3", "Final"]
        count = 1
        for i, exam_type in enumerate(exam_types): # for each mt
            i = i + 1 #zero indexing not for xpath
            for row in table_rows[1:]: # IGNORE FIRST ROW OF TABLE (HEADER) FIND BETTER WAY?
                item = HKNScraperItem()
                item["professor"] = safe_assignment(row, "td[2]/a/text()")
                item["mt_type"] = exam_type
                item["year"] = safe_assignment(row, "td[1]/text()")

                exam_file_loc = 3 + i #td [3 + i]
                item["exam_url"] = safe_assignment(row, "td[3]/a[1]/@href", self.allowed_domains[0])
                item["sol_url"] = safe_assignment(row, "td[3]/a[2]/@href", self.allowed_domains[0])
                yield item
                print(count)
                count+=1
