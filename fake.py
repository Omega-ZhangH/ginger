#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Date    : Jun 11, 2019 17:33
Author  : 张皓
Email   : zhanghao12z@163.com
Function: 通过一个离线脚本实现管理员账号的生成
===========================================
调用方法
Template:
===========================================
"""
from app.models.base import db
from app.models.user import User
from app import create_app

app = create_app()

# 推入上下文
with app.app_context():
    with db.auto_commit():
        user = User()
        user.nickname = 'Super'
        user.auth = 2
        user.email = '999@qq.com'
        user.password = '123456'
        db.session.add(user)
