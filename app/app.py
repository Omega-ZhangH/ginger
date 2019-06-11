#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Date    : Jan 28, 2019 10:13
Author  : 张皓
Email   : zhanghao12z@163.com
Function: 实例化Flask核心对象
===========================================
调用方法
Template:
===========================================
"""


# -*- coding: utf-8 -*-
# @Time    : 2019-01-23 11:59
# @Author  : 张皓
# @Email   : zhanghao12z@163.com
# @File    : __init__.py.py
# @Software: PyCharm

# # 导入蓝图
# def register_blueprints(app):
#     from app.api.v1.user import user
#     from app.api.v1.book import book
#     app.register_blueprint(user)
#     app.register_blueprint(book)

# 重构自定义红图后的蓝图
#from app.api.v1 import create_blueprint_v1
from datetime import date

from flask import Flask as _Flask
from flask.json import JSONEncoder as _JSONEncoder

# 重写flask的JSONEncoder使得
# jsontify支持将对象转换为字典
from app.libs.error_code import ServerError


class JSONEncoder(_JSONEncoder):
    def default(self, o):
        """
        :param o: 为实例化的对象
        :return: o.__dict__
                此处需特别注意，返回的数据只支持 ——> 实力变量
                不支持 --> 类变量
        """
        # return o.__dict__
        # 如果模型里有keys和__getitem__方法才进行返回
        if hasattr(o, 'keys') and hasattr(o, '__getitem__'):
            return dict(o)

        #处理时间类型的数据
        if isinstance(o, date):
            return o.strftime('%Y-%m-%d')
        raise ServerError()


class Flask(_Flask):
    # 重写flask使得自己编写的JSONEncoder能支持
    json_encoder = JSONEncoder

