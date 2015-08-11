#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
创建蓝本
"""

__author__ = 'Hanks'

from flask import Blueprint

main = Blueprint('main', __name__)

from app.models import Permission
from . import views, errors


@main.app_context_processor
def inject_permissions():
    return dict(Permission=Permission)
