#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Date    : May 27, 2019 10:26
Author  : 张皓
Email   : zhanghao12z@163.com
Function: 重写WTForms 自定义错误信息
===========================================
调用方法
Template:
===========================================
"""
from flask import request
from wtforms import Form

from app.libs.error_code import ParameterException


class BaseForm(Form):
    def __init__(self):
        # 直接获取传进来的json数据
        data = request.json
        super(BaseForm, self).__init__(data=data)

    def validate_for_api(self):
        valid = super(BaseForm, self).validate()
        if not valid:
            # 调用form的validate的时候，所有的错误信息会存到errors这个属性里
            # 把报错的errors传入自定义的参数异常方法里
            # 通过此方法，把WTForms不抛出异常的特性，实现抛出异常
            # print(self.errors)
            raise ParameterException(msg=self.errors)
        return self