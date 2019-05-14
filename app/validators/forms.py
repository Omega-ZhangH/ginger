#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Date    : 2019-01-31 17:17
Author  : 张皓
Email   : zhanghao12z@163.com
Function: 验证客户端的合法性
===========================================
调用方法
Template:
===========================================
"""
import json

from wtforms import Form, StringField, IntegerField
from wtforms.validators import DataRequired, length, ValidationError, Email, Regexp

from app.libs.enums import ClientTypeEnum
from app.models.user import User


class ClientForm(Form):
    """
    验证器
    """
    # account : 账号
    # DataRequired()：必传
    # length(min=5, max=32)：参数长度最小为5位，最大为32
    account = StringField(validators=[DataRequired(), length(min=5, max=32)])
    # 密码 ：可为空
    secret = StringField()
    # 账号类型
    type = IntegerField(validators=[DataRequired()])

    # 验证用户传入的账号类型是否在枚举类型里
    # 建议在项目中不要用数字来代表类型，而是用枚举来代表类型
    def validate_type(self, value):
        try:
            client = ClientTypeEnum(value.data)
        except ValueError as e:
            raise e
        # 把转换成枚举类型的数据赋值给账户类型
        self.type.data = client


# 通过新建一个User的验证器，继承ClientForm的基础验证，然后添加一些新的个性化的验证
class UserEmailForm(ClientForm):
    account = StringField(validators=[
        Email(message='invalidate email')
    ])
    secret = StringField(validators=[
        DataRequired(),
        # password can only include letters, numbers and "_", 密码长度是6-22位
        Regexp(r'^[A-Za-z0-9_*&$#@]{6,22}$')
    ])
    nickname = StringField(validators=[DataRequired(),
                                       length(min=2, max=22)])

    # 验证用户是否已经注册
    def validate_account(self, value):
        if User.query.filter_by(email=value.data).first():
            raise ValidationError()

#
# data = {"account": "17126091222",
#         "secret": "222403198502226828",
#         "type": "100"}
#
# data = json.dumps(data, ensure_ascii=False)
# # 如果客户端传送的是json数据，传入数据到验证器则需要用【关键字参数】
# form = ClientForm(data=data)
#
# if form.validate():
#     promise = {
#             ClientTypeEnum.USER_EMAIL: __reister_user_by_email,
#         }
#
#     print(form.type.data)
