#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
sys.path.insert(0, 'lib')
from mysql import MySQL

import ConfigParser
import logging

config = ConfigParser.ConfigParser()
config.read('config/config.cfg')

db_config = config._sections['db']
db_config.pop('__name__')

a = MySQL(**db_config)

# sql = "show tables"
sql = "insert into url (post_id, url, status) values ('11', 'http://www.baidu.com', '0')"
a.query(sql)
a.commit()

# aa = a.get_all(sql)
# print aa

