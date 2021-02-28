# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader import ItemLoader
from itemloaders.processors import TakeFirst, MapCompose
from w3lib.html import remove_tags


class LivescoresItem(scrapy.Item):
    # define the fields for your item here like:
    teams = scrapy.Field()
    game_time = scrapy.Field()
    livescores = scrapy.Field()
    links = scrapy.Field()