# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field  

class TutorialItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

    
class TestspiderItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    url = Field()
    forum = Field()
    poster = Field()
    content = Field()