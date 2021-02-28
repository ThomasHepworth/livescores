# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader import ItemLoader
from itemloaders.processors import TakeFirst, MapCompose
from w3lib.html import remove_tags

# url for the main flashscores website (we're not scraping directly from this)
# links can be pasted to the end of this to pull out further info on the game in a web browser
fs_url = 'https://www.flashscore.co.uk'

# quick function to # concat our links to our flashscores base url (to get the full path)
# match urls only give the end string
def fs_append_links(link_list):
    link_list[:] = ["%s%s" % (fs_url, i) for i in link_list]
    return(link_list)

class LivescoresItem(scrapy.Item):
    # define the fields for your item here like:
    teams = scrapy.Field(input_processor = MapCompose(remove_tags))
    game_time = scrapy.Field(input_processor = MapCompose(remove_tags))
    livescores = scrapy.Field(input_processor = MapCompose(remove_tags))
    links = scrapy.Field(input_processor = MapCompose(remove_tags, fs_append_links))