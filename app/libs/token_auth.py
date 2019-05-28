#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Date    : 2019-05-28 16:11
Author  : 张皓
Email   : zhanghao12z@163.com
Function: 
===========================================
调用方法
Template:
===========================================
"""
from collections import namedtuple

from flask import current_app, g
from flask_httpauth import HTTPBasicAuth
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer, BadSignature, SignatureExpired

from app.libs.error_code import AuthFailed

auth = HTTPBasicAuth()
User = namedtuple('User', ['uid', 'ac_type', 'scope'])


@auth.verify_password
def verify_password(token, paaword):
    user_info = verify_auth_token(token)
    # 如果认证失败的话
    if not user_info:
        return False
    else:
        g.user = user_info
        return True


def verify_auth_token(token):
    # 验证token是否合法
    s = Serializer(current_app.config['SECRET_KEY'])
    try:
        # 载入token
        data = s.loads(token)
    except BadSignature:
        raise AuthFailed(msg='token is invalid',
                         error_code=1002)
    except SignatureExpired:
        raise AuthFailed(msg='token was expired',
                         error_code=1003)
    uid = data['uid']
    ac_type = data['type']
    # 返回结果以对象式的形式返回
    return User(uid, ac_type, '')
