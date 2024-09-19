# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ItemsAndPipelineItem(scrapy.Item):
    # define the fields for your item here like:
    h1 = scrapy.Field()
    h2 = scrapy.Field()
    paragraphs = scrapy.Field()

