#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
入口主文件
Lok 2014/1/10
"""

from flask import Flask
from flask import render_template
from flask import url_for, redirect

app = Flask(__name__)
if not app.debug:
    import logging
    from logging import FileHandler
    from logging import Formatter
    file_handler = FileHandler(filename='logs/index.log')
    file_handler.setFormatter(Formatter(
        '%(asctime)s %(levelname)s: %(message)s '
        '[in %(pathname)s:%(lineno)d]'
    ))
    app.logger.addHandler(file_handler)


@app.route('/')
def link_list():
    return 'link list'

@app.route('/hello')
@app.route('/hello/<name>')
def hello(name=None):
    css = url_for('static', filename='style.css')
    return render_template('hello.html', name=name, css=css)

@app.route('/about')
def about():
    return ''


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)  # in virtualbox