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

from flask import jsonify, g

# # 蓝图实例化
# user = Blueprint('user', __name__)

# 实例化自定义的红图
from app.libs.error_code import DeleteSuccess
from app.libs.redprint import Redprint
from app.libs.token_auth import auth
from app.models.base import db
from app.models.user import User

api = Redprint('user')


@api.route('/<int:uid>', methods=['GET'])
@auth.login_required
def get_user(uid):
    user = User.query.get_or_404(uid)

    return jsonify(user)
    # return jsonify(Name())
    # return 'i'


# 删除用户的操作
@api.route('/', methods=['DELETE'])
@auth.login_required
# 防止超权
# @api.route('/<int:uid>', methods=['DELETE'])
# def delete_user(uid):
def delete_user():
    # 通过g变量来获取,g变量是线程隔离的
    uid = g.user.uid
    with db.auto_commit():
        # 直接调用get_or_404会能反复查询到想要的数据
        # user = User.query.get_or_404(uid)
        # filter_by方法会添加status=1的条件
        user = User.query.filter_by(id=uid).first_or_404()
        user.delete()
    return DeleteSuccess()


# 管理员超级权限
@api.route('/<int:uid>', methods=['DELETE'])
def super_delete_user():
    pass
