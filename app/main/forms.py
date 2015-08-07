#!/usr/bin/env python3
# -*- coding:utf-8 -*-


__author__ = 'Hanks'

from flask.ext.wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required


class NameForm(Form):
    name = StringField('what is you name?', validators=[Required()])
    submit = SubmitField('Submit')
