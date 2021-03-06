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
import datetime

from sqlalchemy import Column, String, SmallInteger, Integer
from werkzeug.security import generate_password_hash, check_password_hash

from app.libs.error_code import NotFound, AuthFailed
from app.models.base import Base, db


class User(Base):
    id = Column(Integer, primary_key=True)
    email = Column(String(24), unique=True, nullable=False)
    nickname = Column(String(24), unique=True)
    # 权限标识:1、普通用户，2、管理员
    auth = Column(SmallInteger, default=1)
    #
    _password = Column('password', String(100))

    # 定义keys，__getattr__ 进行模型序列化时的属性控制
    def keys(self):
        return ['id', 'email', 'nickname', 'auth']




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

    @staticmethod
    def verify(email, password):
        # 验证用户信息，先查找用户信息
        """
        user = User.query.filter_by(email=email).first()
        if not user:
            # 如果没找到用户信息，返回一个自定义的异常
            raise NotFound(msg='用户未找到')
        """
        # 重写first_or_404后，有效精简代码。等价于上面的加if判断
        user = User.query.filter_by(email=email).first_or_404()

        if not user.check_password(password):
            # 如果密码没有找到，在返回一个异常
            raise AuthFailed()
        # 判断是否是管理员
        scope = 'AdminScope' if user.auth == 2 else 'UserScope'
        return {'uid': user.id, 'scope': scope}

    def check_password(self, raw):
        # 定义一个校验用户密码的方法
        if not self._password:
            return False
        return check_password_hash(self._password, raw)

    def delete(self):
        # 软删除
        self.status = 0
