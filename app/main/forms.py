#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from app.models import User, Role
from flask.ext.pagedown.fields import PageDownField

__author__ = 'Hanks'

from flask.ext.wtf import Form
from wtforms import StringField, SubmitField, TextAreaField, BooleanField, SelectField
from wtforms.validators import Required, Length, Email, Regexp, ValidationError


class NameForm(Form):
    name = StringField('what is you name?', validators=[Required()])
    submit = SubmitField('Submit')


class PostForm(Form):
    body = PageDownField('记录下你所想的...', validators=[Required()])
    submit = SubmitField('完成')


class EditProfileForm(Form):
    name = StringField('真实姓名', validators=[Length(0, 64)])
    location = StringField('所在城市', validators=[Length(0, 64)])
    about_me = TextAreaField('关于我')
    submit = SubmitField('完成')


class EditProfileAdminForm(Form):
    email = StringField('Email', validators=[Required(), Length(1, 64),
                                             Email()])
    username = StringField('Username', validators=[
        Required(), Length(1, 64), Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0,
                                          'Usernames must have only letters, '
                                          'numbers, dots or underscores')])
    confirmed = BooleanField('已通过验证')
    role = SelectField('Role', coerce=int)
    name = StringField('真实姓名', validators=[Length(0, 64)])
    location = StringField('所在城市', validators=[Length(0, 64)])
    about_me = TextAreaField('关于我')
    submit = SubmitField('完成')

    def __init__(self, user, *args, **kwargs):
        super(EditProfileAdminForm, self).__init__(*args, **kwargs)
        self.role.choices = [(role.id, role.name)
                             for role in Role.query.order_by(Role.name).all()]
        self.user = user

    def validate_email(self, field):
        if field.data != self.user.email and \
                User.query.filter_by(email=field.data).first():
            raise ValidationError('邮箱已被注册.')

    def validate_username(self, field):
        if field.data != self.user.username and \
                User.query.filter_by(username=field.data).first():
            raise ValidationError('用户名已被占用')


class CommentForm(Form):
    body = StringField('', validators=[Required()])
    submit = SubmitField('完成')
