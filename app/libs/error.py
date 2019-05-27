#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Date    : 2019-05-15 17:18:27
Author  : 张皓
Email   : zhanghao12z@163.com
Function:
===========================================
调用方法
Template:
===========================================
"""
# 注意此处要用werkzeug的库，而不是http.client
from flask import request, json
from werkzeug.exceptions import HTTPException


class APIException(HTTPException):
    code = 500
    msg = 'sorry, we make a mistake ^_^！'
    error_code = 999

    def __init__(self, msg=None, code=None, error_code=None, headers=None):
        # 如果传值了则用传的值，否则用默认定义的值
        if code:
            self.code = code
        if error_code:
            self.error_code = error_code
        if msg:
            self.msg = msg

        super(APIException, self).__init__(msg, None)

    def get_body(self, environ=None):
        """Get the Json body."""
        body = dict(
            msg=self.msg,
            error_code=self.error_code,
            request=request.method + ' ' + self.get_url_no_param()
        )

        text = json.dumps(body)
        return text

    @staticmethod
    def get_url_no_param():
        full_path = str(request.full_path)
        main_path = full_path.split('?')
        return main_path[0]

    def get_headers(self, environ=None):
        """Get a list of headers."""
        return [('Content-Type', 'application/json ')]