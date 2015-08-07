#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
创建蓝本
"""

__author__ = 'Hanks'

from flask import Blueprint

main = Blueprint('main', __name__)

from . import views, errors
