#!/usr/bin/env python
# -*- coding: utf-8 -*-

import ConfigParser

class Common:
    _db = None
    def __init__(self):
        pass
    
    def init_db(self):
        config = ConfigParser.ConfigParser()
        config.read('/media/crawler/config/config.cfg')
        db_config = config._sections['db']
        db_config.pop('__name__')
        from mysql import MySQL
        self._db = MySQL(**db_config)
        return self._db
    
    def get_urls(self, status=0):
        sql = "SELECT url FROM url WHERE status='%s'" % status
        urls = self._db.get_all(sql)
        ret = []
        if urls:
            for i in urls:
                ret.append(i['url'])
        return ret
        
