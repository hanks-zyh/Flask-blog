#!/usr/bin/env python3
# -*- coding:utf-8 -*-

__author__ = 'Hanks'

from flask import Blueprint

auth = Blueprint('auth', __name__)

from . import views

