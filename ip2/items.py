# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Ip2Item(scrapy.Item):
    # define the fields for your item here like:
    ip = scrapy.Field()
    post = scrapy.Field()
    tcp = scrapy.Field()
    # name = scrapy.Field()
    # name = scrapy.Field()
    # name = scrapy.Field()
    # name = scrapy.Field()
    pass