#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from app.models import Permission

__author__ = 'Hanks'

from functools import wraps
from flask import abort
from flask.ext.login import current_user


def permission_require(permission):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if not current_user.can(permission):
                abort(403)
            return f(*args, **kwargs)

        return decorated_function

    return decorator


def admin_require(f):
    return permission_require(Permission.ADMINISTER)(f)
