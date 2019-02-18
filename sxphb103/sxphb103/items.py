# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy



class ProvinceItem(scrapy.Item):
    provincename = scrapy.Field()
class Sxphb103Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()
    money = scrapy.Field()
    province = scrapy.Field()