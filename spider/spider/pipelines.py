# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


from scrapy import log
from common import Common

class SpiderPipeline(object):
    _db = None
    
    def __init__(self):
        self._db = Common().init_db()
    
    def process_item(self, item, spider):
        log.msg('spider: %s' % spider.name, log.DEBUG)
        if spider.name == 'voa_link':
            sql = "INSERT INTO url (post_id, url) VALUES ('%s', '%s')" % (item['post_id'], item['url'])
            self._db.query(sql)
            self._db.commit()
        else:
            log.msg('url %s' % item['url'], log.DEBUG)
        return item
    
    
