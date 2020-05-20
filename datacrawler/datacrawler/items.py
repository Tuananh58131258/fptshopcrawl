# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DatacrawlerItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    ten = scrapy.Field()
    url_img = scrapy.Field()
    gia = scrapy.Field()
    gia_online = scrapy.Field()
    gia_cu = scrapy.Field()
    khuyen_mai = scrapy.Field()
    data = scrapy.Field()
    ram = scrapy.Field()
    rom = scrapy.Field()
    label = scrapy.Field()
    mau_sac = scrapy.Field()
    pass
