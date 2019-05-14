#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Date    : Jan 28, 2019 09:47
Author  : 张皓
Email   : zhanghao12z@163.com
Function: 配置关键配置项
===========================================
调用方法
Template:
===========================================
"""

# 数据库连接
USERNAME = 'mstx'
PASSWORD = 'mstx'
HOSTNAME = 'localhost'
PORT = 63306
DATABASE = 'ginger'

SQLALCHEMY_DATABASE_URI = "mysql+cymysql://{username}:{password}@{host}:{port}/" \
         "{db}?charset=utf8".format(username=USERNAME,
                                    password=PASSWORD,
                                    host=HOSTNAME,
                                    port=PORT,
                                    db=DATABASE)

SECRET_KEY = 'e10adc3949ba59abbe56e057f20f883e'

SQLALCHEMY_TRACK_MODIFICATIONS = True