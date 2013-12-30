# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field

class SpiderItem(Item):
    # define the fields for your item here like:
    # name = Field()
    pass


class LinkItem(Item):
    post_id = Field()
    url = Field()
    

class ContentItem(Item):
    add_time = Field()
    post_id = Field()
    title = Field()
    keywords = Field()
    desc = Field()
    content = Field()
    