# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import sys
sys.path.insert(0, '/media/crawler/lib')
import ConfigParser

from mysql import MySQL
from scrapy import log


class SpiderPipeline(object):
    _db = None
    
    def __init__(self):
        config = ConfigParser.ConfigParser()
        config.read('/media/crawler/config/config.cfg')
        db_config = config._sections['db']
        db_config.pop('__name__')
        self._db = MySQL(**db_config)
        log.start('/media/crawler/logs/scrapy.log')
    
    def process_item(self, item, spider):
        log.msg("url: %s" % item['url'], level=log.DEBUG)
        return item
    
    
