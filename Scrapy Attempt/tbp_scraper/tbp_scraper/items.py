# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Item, Field


class TbpScraperItem(scrapy.Item):
    # define the fields for your item here like:
    year = Field()
    professor = Field()
    exam_type = Field()
    exam_url = Field()
    sol_url = Field()


class HKNScraperItem(scrapy.Item):
    # define the fields for your item here like:
    year = Field()
    professor = Field()
    exam_type = Field()
    exam_url = Field()
    sol_url = Field()
