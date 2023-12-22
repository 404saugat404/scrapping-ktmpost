# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Ktmprost2Item(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    title2 = scrapy.Field()
    news_details = scrapy.Field()
    img_links = scrapy.Field()
    
