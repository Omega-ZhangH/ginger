#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Date    : 2019-02-25 16:49
Author  : 张皓
Email   : zhanghao12z@163.com
Function: 
===========================================
调用方法
Template:
===========================================
"""
from sqlalchemy import Column, String, SmallInteger, Integer
from werkzeug.security import generate_password_hash

from app.models.base import Base, db


class User(Base):
    id = Column(Integer, primary_key=True)
    email = Column(String(24), unique=True, nullable=False)
    nickname = Column(String(24), unique=True)
    # 权限标识:1、普通用户，2、管理员
    auth = Column(SmallInteger, default=1)
    #
    _password = Column('password', String(100))

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, raw):
        self._password = generate_password_hash(raw)

    @staticmethod
    def register_by_email(nickname, account, secret):
        with db.auto_commit():
            user = User()
            user.nickname = nickname
            user.email = account
            user.password = secret
            db.session.add(user)
