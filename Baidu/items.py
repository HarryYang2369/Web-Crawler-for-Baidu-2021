# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BaiduItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    subject = scrapy.Field()
    url = scrapy.Field()
    title = scrapy.Field()
    source = scrapy.Field()
    publish_time = scrapy.Field()
    brief = scrapy.Field()

