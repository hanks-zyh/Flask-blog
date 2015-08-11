#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from os import abort
from flask.ext.login import current_user

__author__ = 'Hanks'

from datetime import datetime
from flask import render_template, session, redirect, url_for, current_app, request

from . import main
from .forms import NameForm, PostForm
from .. import db
from ..models import User, Role, Permission, Post
from ..email import send_email


@main.route('/', methods=['GET', 'POST'])
def index():
    form = PostForm()
    if current_user.can(Permission.WRITE_ARTICLES) and form.validate_on_submit():
        post = Post(body=form.body.data, author=current_user._get_current_object())
        db.session.add(post)
        return redirect(url_for('main.index'))
    # posts = Post.query.order_by(Post.timestamp.desc()).all()
    page = request.args.get('page', 1, type=int)
    pagination = Post.query.order_by(Post.timestamp.desc()).paginate(
        page, per_page=current_app.config['FLASKY_POSTS_PER_PAGE'],
        error_out=False)
    posts = pagination.items
    return render_template('index.html', form=form, posts=posts, pagination=pagination)


@main.route('/user/<username>')
def user(username):
    user = User.query.filter_by(username=username).first()
    if user is None:
        abort(404)
    return render_template('user.html', user=user)
