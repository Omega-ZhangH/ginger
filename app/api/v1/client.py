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
from app.libs.error import APIException
from app.libs.error_code import ClientTypeError, Success
from app.libs.redprint import Redprint
from app.models.user import User
from app.validators.forms import UserEmailForm, ClientForm

api = Redprint('client')


@api.route('/register', methods=['POST'])
def create_client():
    # request.json的数据隐藏在了ClientForm的基类中直接调用，简化调用
    form = ClientForm()
    form.validate_for_api()
    promise = {
        ClientTypeEnum.USER_EMAIL: __reister_user_by_email,
    }
# 调用__reister_user_by_email方法，通过枚举类型拿到
    promise[form.type.data]()

    # return一个类本质是返回的一个HTTPException 实际上是一个html返回
    return Success()


# 邮箱客户端验证
def __reister_user_by_email():
    form = UserEmailForm().validate_for_api()
    # if form.validate():
    # 通过新编些的方法来验证
    # 注册用户信息写入到数据库
    User.register_by_email(form.nickname.data,
                           form.account.data,
                           form.secret.data)

