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
