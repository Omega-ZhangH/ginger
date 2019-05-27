#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Date    : 2019-05-14 17:05:06
Author  : 张皓
Email   : zhanghao12z@163.com
Function:
===========================================
调用方法
Template:
===========================================
"""
# 注意此处要用werkzeug的库，而不是http.client
from werkzeug.exceptions import HTTPException

from app.libs.error import APIException


class Success(APIException):
    # 定义一个操作成功的反馈信息
    code = 201
    msg = 'OK'
    error_code = 0


class ServerError(APIException):
    # 专门定义一个异常的返回，作用等同于APIException
    # 但是名称规范，增加维护的可读性
    code = 500
    msg = 'sorry, we make a mistake ^_^！'
    error_code = 999


class ClientTypeError(HTTPException):
    # 400:请求参数错误
    # 401:未授权
    # 403：禁止访问
    # 404：没有找到资源或页面
    # 500：服务器产生的未知错误
    # 200：查询成功
    # 201：创建或更新成功
    # 204：删除成功
    # 301、302：重定向
    code = 400

    description = {
        'client is invalid'
    }


class ParameterException(APIException):
    code = 400
    msg = 'invalid parameter'
    error_code = 1000
