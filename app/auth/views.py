#!/usr/bin/env python3
# -*- coding:utf-8 -*-

__author__ = 'Hanks'

from flask import render_template
from . import auth


@auth.route('/login')
def login():
    render_template('auth/login.html')
