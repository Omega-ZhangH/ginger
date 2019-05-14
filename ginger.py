#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Date    : Jan 28, 2019 09:52
Author  : 张皓
Email   : zhanghao12z@163.com
Function:
===========================================
调用方法
Template:
===========================================
"""


from app import create_app

app = create_app()


if __name__ == '__main__':
    app.run(debug=True)
