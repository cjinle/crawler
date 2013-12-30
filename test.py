#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
sys.path.insert(0, 'lib')

from mysql import MySQL

config = {'hello':'world'}

a = MySQL(**config)

print a

