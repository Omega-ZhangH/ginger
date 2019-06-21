#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Date    : 2019-05-14 17:05:06
Author  : 张皓
Email   : zhanghao12z@163.com
Function:
===========================================
调用方法
Template:
===========================================
"""
# 注意此处要用werkzeug的库，而不是http.client
from werkzeug.exceptions import HTTPException

from app.libs.error import APIException


class Success(APIException):
    # 定义一个操作成功的反馈信息
    code = 201
    msg = 'OK'
    error_code = 0


class DeleteSuccess(Success):
    # 定义一个删除操作成功的反馈信息
    # 如果定义成204则前端不会返回内容，因为html协议中定义的204状态就是无信息
    # 为了保持API的返回一致性，定义成别的code
    # code = 204
    code = 202
    error_code = 1


class ServerError(APIException):
    # 专门定义一个异常的返回，作用等同于APIException
    # 但是名称规范，增加维护的可读性
    code = 500
    msg = 'sorry, we make a mistake ^_^！'
    error_code = 999


class ClientTypeError(HTTPException):
    # 400:请求参数错误
    # 401:未授权
    # 403：禁止访问
    # 404：没有找到资源或页面
    # 500：服务器产生的未知错误
    # 200：查询成功
    # 201：创建或更新成功
    # 204：删除成功
    # 301、302：重定向
    code = 400

    description = {
        'client is invalid'
    }


class ParameterException(APIException):
    # 自定义一个参数异常类
    code = 400
    msg = 'invalid parameter'
    error_code = 1000


class NotFound(APIException):
    # 自定义一个未查到的异常类
    code = 404
    msg = 'the resource are not found 0_0...'
    error_code = 1001


class AuthFailed(APIException):
    # 自定义一个授权失败的异常类
    code = 401
    msg = 'authorization failed'
    error_code = 1005


class Forbidden(APIException):
    # 自定义一个禁止访问，权限不够的异常类
    code = 403
    msg = 'forbidden, not in scope'
    error_code = 1004

