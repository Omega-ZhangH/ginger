#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Date    : 2019-01-31 17:24
Author  : 张皓
Email   : zhanghao12z@163.com
Function: 
===========================================
调用方法
Template:
===========================================
"""

from enum import Enum


class ClientTypeEnum(Enum):
    USER_EMAIL = 100
    USER_MOBILE = 101
    # 微信小程序
    USER_MINA = 200
    # 微信公众号
    USER_WX = 201



