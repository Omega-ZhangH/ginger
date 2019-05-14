#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Date    : 2019-01-28 10:07
Author  : 张皓
Email   : zhanghao12z@163.com
Function: 配置关键配置项
===========================================
调用方法
Template:
===========================================
"""
from flask import Blueprint
from app.api.v1 import book, user, client


# 定义一个蓝图
def create_blueprint_v1():

    # 实例化一个红图公用的蓝图
    bp_v1 = Blueprint('v1', __name__)
    # 把红图注册到蓝图
    # user.api.register(bp_v1, url_prefix='/user')
    # book.api.register(bp_v1, url_prefix='/book')

    # 把红图注册到蓝图,优化url_prefix
    user.api.register(bp_v1)
    book.api.register(bp_v1)
    client.api.register(bp_v1)

    return bp_v1
