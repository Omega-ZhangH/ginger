#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Date    : 2019-01-28 10:08
Author  : 张皓
Email   : zhanghao12z@163.com
Function:
===========================================
调用方法
Template:
===========================================
"""
from flask import Blueprint

# # 蓝图实例化
# from app.libs.redprint import Redprint
#
# book = Blueprint('book', __name__)


# 实例化自定义的红图
from app.libs.redprint import Redprint

api = Redprint('book')


@api.route('/get')
def get_book():
    return 'i am book'
