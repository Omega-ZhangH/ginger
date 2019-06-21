#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Date    : 2019-01-28 10:57
Author  : 张皓
Email   : zhanghao12z@163.com
Function: 创建红图文件
===========================================
调用方法
Template:
===========================================
"""


class Redprint:
    """
    模仿蓝图来实现红图
    """
    def __init__(self, name):
        self.name = name
        self.mound = []

    def route(self, rule, **options):
        """
        :param rule: url地址
        :param options: 传入可变关键字参数，**options解包后为字典
        :return:
        """
        def decorator(f):
            # 此处在列表添加的是元组，以备后续打卡
            self.mound.append((f, rule, options))
            return f
        return decorator

    def register(self, blueprint, url_prefix=None):
        """
        :param blueprint: 传入蓝图
        :param url_prefix: 传入红图的URL前缀
        :return:
        """
        # 默认添加url前缀为实例名
        if url_prefix is None:
            url_prefix = '/' + self.name

        for f, rule, options in self.mound:
            # options是字典，pop是删除如果有endpoint的key，返回对应的值，否则返回默认值
            # endpoint = options.pop("endpoint", f.__name__)
            # 修改endpoint的格式，变成：红图名字+视图名字
            endpoint = self.name + '+' + options.pop("endpoint", f.__name__)
            blueprint.add_url_rule(url_prefix + rule, endpoint, f, **options)
