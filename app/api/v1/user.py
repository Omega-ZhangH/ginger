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
# user = Blueprint('user', __name__)

# 实例化自定义的红图
from app.libs.redprint import Redprint
from app.libs.token_auth import auth

api = Redprint('user')


@api.route('', methods=['GET'])
@auth.login_required
def get_user():
    return 'i am user'
