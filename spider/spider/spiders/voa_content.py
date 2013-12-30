from scrapy.selector import Selector
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule
from spider.items import ContentItem

class VoaContentSpider(CrawlSpider):
    name = 'voa_content'
    allowed_domains = ['51voa.com']
    start_urls = ['http://www.51voa.com/']

    rules = (
        Rule(SgmlLinkExtractor(allow=r'VOA_Special_English/'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        sel = Selector(response)
        i = ContentItem()
        i['title'] = sel.select("//div[@id='title']/text()").extract()[0]
        i['keywords'] = ''
        i['desc'] = ''
        i['content'] = ''
        
        #i['domain_id'] = sel.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = sel.xpath('//div[@id="name"]').extract()
        #i['description'] = sel.xpath('//div[@id="description"]').extract()
        return i
