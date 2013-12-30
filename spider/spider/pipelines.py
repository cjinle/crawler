# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import sys
sys.path.insert(0, '../../lib')
import ConfigParser
import logging

from mysql import MySQL


class SpiderPipeline(object):
    _db = None
    
    def __init__(self):
        config = ConfigParser.ConfigParser()
        config.read('../../config/config.cfg')
        db_config = config._sections['db']
        db_config.pop('__name__')
        self._db = MySQL(**db_config)
    
    def process_item(self, item, spider):
        print item
        
        return item
    
    
