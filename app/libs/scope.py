#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Date    : 2019-06-18 14:38:23
Author  : 张皓
Email   : zhanghao12z@163.com
Function: 定义用户权限作用域
===========================================
调用方法
Template:
===========================================
"""


# 定义一个基类，让权限相加的操作都能支持
class Scope:
    allow_api = []
    allow_module = []
    forbidden = []
    # def add(self, other):
    def __add__(self, other):
        # 运算符重载，支持对象的相加
        self.allow_api = self.allow_api + other.allow_api
        self.allow_api = list(set(self.allow_api))

        self.allow_module = self.allow_module + other.allow_module
        self.allow_module = list(set(self.allow_module))

        self.forbidden = self.forbidden + other.forbidden
        self.forbidden = list(set(self.forbidden))
        return self


# 定义管理员可访问的视图列表
class AdminScope(Scope):
    # allow_api = ['v1.super_get_user', 'v1.get_user']
    allow_module = ['v1.user']
    # 权限相加
    def __init__(self):
        # self.add(UserScope())
        self + UserScope()


# 定义普通用户可访问的视图列表
class UserScope(Scope):
    forbidden = ['v1.user+super_get_user', 'v1.user+super_delete_user']

    def __init__(self):
        self + AdminScope()



def is_in_scope(scope, endpoint):
    '''
    :param scope (str):传入解析toKen中的scope的值
    :param endpoint: 视图函数的目录
    '''
    # 通过一个类的名字而得到一个类的对象：
    scope = globals()[scope]()

    # 获取红图
    splits = endpoint.split('+')
    redname = splits[0]

    if endpoint in scope.forbidden:
        return False
    if endpoint in scope.allow_api:
        return True
    if redname in scope.allow_module:
        return True
    else:
        return False
