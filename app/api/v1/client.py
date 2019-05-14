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

# 实例化自定义的红图
from flask import request

from app.libs.enums import ClientTypeEnum
from app.libs.error_code import ClientTypeError
from app.libs.redprint import Redprint
from app.models.user import User
from app.validators.forms import UserEmailForm, ClientForm

api = Redprint('client')


@api.route('/register', methods=['POST'])
def create_client():
    data = request.json
    # 如果客户端传送的是json数据，传入数据到验证器则需要用【关键字参数】
    form = ClientForm(data=data)

    if form.validate():
        promise = {
            ClientTypeEnum.USER_EMAIL: __reister_user_by_email,
        }
    # 调用__reister_user_by_email方法，通过枚举类型拿到
        promise[form.type.data]()
    else:
        raise ClientTypeError()
    return 'success'


# 邮箱客户端验证
def __reister_user_by_email():
    form = UserEmailForm(data=request.json)
    if form.validate():
        User.register_by_email(form.nickname.data,
                               form.account.data,
                               form.secret.data)
