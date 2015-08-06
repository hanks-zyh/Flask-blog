#!/usr/bin/env python3
# -*- coding:utf-8 -*-


__author__ = 'Hanks'

from flask import Flask
from flask.ext.script import Manager
from flask import render_template
from flask.ext.bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)


# manager = Manager(app)

@app.errorhandler(404)
def page_not_found(e):
    render_template('404.html'), 404


@app.errorhandler(500)
def page_not_found(e):
    render_template('500.html'), 500


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)


if __name__ == '__main__':
    #   manager.run()
    app.run()
