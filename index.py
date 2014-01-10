#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
入口主文件
Lok 2014/1/10
"""


from flask import Flask

app = Flask(__name__)
if not app.debug:
    import logging
    from logging import FileHandler
    from logging import Formatter
    file_handler = FileHandler(filename='./log.log')
    file_handler.setFormatter(Formatter(
        '%(asctime)s %(levelname)s: %(message)s '
        '[in %(pathname)s:%(lineno)d]'
    ))
    app.logger.addHandler(file_handler)


@app.route('/')
def link_list():
    return 'link list'

@app.route('/hello')
def hello():
    app.logger.error("hello ............ ")
    return 'hello world'


if __name__ == '__main__':
    app.run(host='0.0.0.0')  # in virtualbox