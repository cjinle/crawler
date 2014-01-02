from scrapy.spider import BaseSpider
from scrapy.selector import Selector
from spider.items import LinkItem

class VoaLinkSpider(BaseSpider):
    name = "voa_link"
    allowed_domains = ["51voa.com"]
    start_urls = (
        'http://www.51voa.com/',
        )

    def parse(self, response):
        sel = Selector(response)
        urls = sel.xpath("//div[@id='list']/ul/li/a[last()]/@href").extract()
        tmp = []
        if urls:
            for i in urls:
                li = LinkItem()
                li['post_id'] = i.split('-')[-1].split('.')[0]
                li['url'] = i
                tmp.append(li)
        return tmp
                
                
