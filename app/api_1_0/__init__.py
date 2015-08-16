#!/usr/bin/env python3
# -*- coding:utf-8 -*-

__author__ = 'Hanks'

from flask import Blueprint

api = Blueprint('api', __name__)

from . import authentication, users, posts, comments, errors
