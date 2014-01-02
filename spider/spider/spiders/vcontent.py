from scrapy.spider import BaseSpider
from scrapy.selector import Selector
from spider.items import ContentItem
from scrapy import log

from common import Common

class VcontentSpider(BaseSpider):
    name = "vcontent"
    allowed_domains = ["51voa.com"]
    start_urls = (
            'http://www.51voa.com/Voa_English_Learning/south-sudan-government-and-rebels-to-hold-talks-to-end-violence-54269.html',
            'http://www.51voa.com/VOA_Standard_English/the-year-in-roots-music-54272.html',
            'http://www.51voa.com/VOA_Standard_English/the-year-in-roots-music-54272.html',
        )

    def parse(self, response):
        sel = Selector(response)
        log.msg("response: %s" % str(dir(response)))
#         i = ContentItem()
#         
#         return i
