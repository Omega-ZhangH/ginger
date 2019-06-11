#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Date    : 2019-05-27 17:39:15
Author  : 张皓
Email   : zhanghao12z@163.com
Function: 编写生成token
===========================================
调用方法
Template:
===========================================
"""
from flask import current_app, jsonify

from app.libs.enums import ClientTypeEnum
from app.libs.redprint import Redprint
from app.models.user import User
from app.validators.forms import ClientForm
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer

api = Redprint('token')


@api.route('', methods=['POST'])
# 之所以用POST方法是为了隐藏用户名密码，可以放在BODY中传.传参更安全
def get_token():
    """
    :return: 返回加密后的Token和一个HTTP状态码
    """
    # api的get_token就相当于web的login
    # 接收用户的参数
    form = ClientForm().validate_for_api()

    promise = {
        ClientTypeEnum.USER_EMAIL: User.verify
    }

    identity = promise[ClientTypeEnum(form.type.data)](
        form.account.data,
        form.secret.data
    )

    # 生成Token
    token = generate_auth_token(identity['uid'],
                                form.type.data,
                                expiration=current_app.config['TOKEN_EXPIRATION'])
    # 将Token字节码转换为ascii码
    t = {
        'token': token.decode('ascii'),
        'uid': identity['uid']
    }

    return jsonify(t), 201


def generate_auth_token(uid, ac_type, scope=None, expiration=7200):
    """
    生成Token
    :param uid: 用户ID
    :param ac_type: 账户类型
    :param scope: 权限作用域
    :param expiration: 有效时间
    :return: 返回加密后的Token
    """
    s = Serializer(current_app.config['SECRET_KEY'],
                   expires_in=expiration)
    return s.dumps({
        'uid': uid,
        'type': ac_type.value
    })
