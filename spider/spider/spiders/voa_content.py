from scrapy.spider import BaseSpider
from scrapy.selector import Selector
from spider.items import ContentItem
from scrapy import log

from common import Common

class VoaContentSpider(BaseSpider):
    name = 'voa_content'
    allowed_domains = ['51voa.com']
    start_urls = [
                  'http://www.51voa.com/Voa_English_Learning/south-sudan-government-and-rebels-to-hold-talks-to-end-violence-54269.html',
                  'http://www.51voa.com/VOA_Standard_English/the-year-in-roots-music-54272.html',
                  'http://www.51voa.com/VOA_Standard_English/the-year-in-roots-music-54272.html',
                  ]
    
    def __init__(self):
        pass
#         c = Common()
#         c.init_db()
#         self.start_urls = [ 'http://www.51voa.com%s' % i for i in c.get_urls() ]

    def parse_item(self, response):
        sel = Selector(response)
        self.log.msg("url: %s" % response.url)
        i = ContentItem()
        i['title'] = sel.select("//div[@id='title']/text()").extract()[0]
        i['keywords'] = ''
        i['desc'] = ''
        i['content'] = ''
        return i
