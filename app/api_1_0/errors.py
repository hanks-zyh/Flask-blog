#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from . import api
from app.exceptions import ValidationError
from flask import jsonify

__author__ = 'Hanks'


#
# HTTP状态码 | 名称                               |  说　　明
# 200        OK（成功）                             请求成功完成
# 201        Created（已创建）                      请求成功完成并创建了一个新资源
# 400        Bad request （坏请求）                 请求不可用或不一致
# 401        Unauthorized（未授权）                 请求未包含认证信息
# 403        Forbidden（禁止）                      请求中发送的认证密令无权访问目标
# 404        Notfound （未找到）                    URL对应的资源不存在
# 405        Method not allowed（不允许使用的方法）   指定资源不支持请求使用的方法
# 500        Internal server error （内部服务器错误） 处理请求的过程中发生意外错误

def bad_request(message):
    response = jsonify({'error': 'bad request', 'message': message})
    response.status_code = 400
    return response


def unauthorized(message):
    response = jsonify({'error': 'unathorized', 'message': message})
    response.status_code = 401
    return response


def forbidden(message):
    response = jsonify({'error': 'forbidden', 'message': message})
    response.status_code = 403
    return response


@api.errorhandler(ValidationError)
def validation_error(e):
    return bad_request(e.args[0])
