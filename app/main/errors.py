#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
蓝本中的错误处理程序
"""
__author__ = 'Hanks'

from flask import render_template
from . import main


@main.app_errorhandler(404)
def page_not_found(e):
    render_template('404.html'), 404


@main.app_errorhandler(500)
def page_not_found(e):
    render_template('500.html'), 500
