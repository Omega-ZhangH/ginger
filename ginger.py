#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Date    : Jan 28, 2019 09:52
Author  : 张皓
Email   : zhanghao12z@163.com
Function:
===========================================
调用方法
Template:
===========================================
"""
from werkzeug.exceptions import HTTPException

from app import create_app
from app.libs.error import APIException
from app.libs.error_code import ServerError

app = create_app()


# 全局异常处理
@app.errorhandler(Exception)
def framework_error(e):
    # flask 1.0 可以捕捉通用的异常
    # 判断属于哪种异常
    if isinstance(e, APIException):
        return e
    if isinstance(e, HTTPException):
        code = e.code
        msg = e.description
        error_code = 1007
        return APIException(code=code, msg=msg, error_code=error_code)
    else:
        # return APIException()
        # 作用等同于APIException，可读性更强
        # 还要注意的一点，如果是在调试模式下，是需要把完整的报错返回出来
        if not app.config['DEBUG']:
            return ServerError()
        else:
            raise e


if __name__ == '__main__':
    app.run(debug=True)
    # app.run(debug=False)
