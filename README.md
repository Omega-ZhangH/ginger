### Flask编写具有可扩展性的RESTfulAPI

```
Date    : Jan 23, 2019 11:13
Author  : 张皓
Email   : zhanghao12z@163.com
===========================================
简介     : 深入了解Python3
          编写可扩展的RESTful API
===========================================
```

#### 1-1 Flask VS Django

- 框架效率对比
  - 常用的插件安装在flask上那就和Django基本上一致了
- 框架的优秀程度
  - GitHub Stars数量几乎相同
  - 同样被开发者广泛使用
- 上手速度
  - Django模块集成的比较全
  - Flask内置插件小，灵活的更高
- 谁更适合做大型项目
  - 大型项目基本上跨语言、跨架构
- 取舍
  - 选一个框架，学精
  - 另外一个框架了解即可

#### 2-1 环境、开发工具与flask1.0

[开发工具]

1. 编译换件: 	Python 3.6(推荐虚拟环境：pipenv)
2. 开发工具：     Pycharm and VS code
3. MySQL工具：Xampp或自建的MySQL数据库
4. 数据库可视化管理工具：Navicat or DataGrip
5. API测试工具：PostMan

[Package]

- Flask1.0

#### 2-2 初始化项目

- 安装Python
- 使用pip安装pipenv
- 新建项目目录（ginger）
- 进入项目目录
- 使用pipenv install 命令创建虚拟环境。先把Pipfile放到项目目录，就会直接安装所有项目的依赖包
- 查看已安装的包的命令：pipenv graph
- 查看虚拟环境名字的命令：pipenv --venv

#### 2-3 新建入口文件

- app ：主程序文件夹
  - \__init__.py : 核心对象初始化及加载配置文件
  - config ：新建配置文件
    - setting : 存放普通设置
    - secure : 存放保密设置
- ginger : 入口文件

#### 2-4 蓝图分离视图函数的缺陷

> 2019-01-28 10:40:19

- 视图函数集中在一个文件中，则必然臃肿不堪，且极难维护
- 对于模型多的项目，无法分门别类
  - 蓝图拆分视图函数的缺点：
    - 蓝图应该是模块级别的拆分：如用户管理模块、业务模块等
    - 蓝图分割下的URL地址长且，前半部分会有冗余

- app ：主程序文件夹
  - \__init__.py : 核心对象初始化及加载配置文件
  - config ：新建配置文件
    - setting : 存放普通设置
    - secure : 存放保密设置
  - **api** : 应用接口文件夹（新建）
    - **v1** ：版本文件夹
      - **book** ：存放书籍相关视图函数
      - **user** ： 存放用户相关视图函数
- ginger : 入口文件

#### 2-5 打开思维，创建自己的Redprint——红图

- app ：主程序文件夹
  - \__init__.py : 核心对象初始化及加载配置文件
  - config ：新建配置文件
    - setting : 存放普通设置
    - secure : 存放保密设置
  - api : 应用接口文件夹
    - v1 ：版本文件夹
      - **\__init__** : 统一蓝图的实例化和红图注册
      - book ：存放书籍相关视图函数
      - user ： 存放用户相关视图函数
  - **libs** : 存放自定义模块（新建）
    - **redprint** :  用于编写自定义红图，拆分视图函数
- ginger : 入口文件

> 自定义红图的结构图

- app
  - 蓝图（prefix_url:解决url过长）
    - 红图（prefix_url:解决url过长）
      - 视图函数

#### 2-6 实现Redprint

> 2019-01-29 11:42:49

- class Redprint :  编写红图类
  - route（）：编写注册路由的函数
  - register（）：编写注册红图到蓝图的函数

#### 2-7 优化Redprint

> 优化url地址的前缀，设置默认值为'/' + 红图名

```python
        # 默认添加url前缀为实例名
        if url_prefix is None:
            url_prefix = '/' + self.name
```

#### 3-1 REST的最基本特征

- REST : 表述性状态转移
  - **强制要求要返回JSON格式**
  - **可读性非常强的URL设计**
  - 使用URL来定位资源
    - URL中尽量不要包含动词
    - **要包含版本号**
      - 可以放在浏览器HEADERS
      - 也可以放在URL中
      - 也可以放在？后面作为查询参数
  - 通过HTTP动词来调用资源
    - GET
    - POST
    - PUT
    - DELETE

####3-2 为什么标准REST不适合内部开发

- REST并不是适合所有场景
  - 不适合的场景和缺点
    - 接口粒度比较粗
      - REST接口只返回数据，可能会多返回冗余数据，同时也不规整数据（如性别为1，代表男，但接口只返回1）
      - 业务逻辑复杂，会导致HTTP请求量会大幅度增加
    - 内部开发
    - 用四个视图函数 增删改查 无法适配复杂业务逻辑
  - 适合的场景
    - 开放性的API ：只提供数据，不关心业务逻辑
      - 豆瓣
      - 微博
      - github

#### 4-1 关于“用户”的思考

- API的
  - 特性
    - **开放性**
    - **通用性**
  - 用户：统称客户端**[client]**
    - 人
    - 第三方APP
    - 小程序
    - 自己的产品

#### 4-2 构建Client验证器

> 2019-01-31 17:50:09

- app ：主程序文件夹
  - \__init__.py : 核心对象初始化及加载配置文件
  - config ：新建配置文件
    - setting : 存放普通设置
    - secure : 存放保密设置
  - api : 应用接口文件夹（新建）
    - v1 ：版本文件夹
      - book ：存放书籍相关视图函数
      - user ： 存放用户相关视图函数
  - **libs** ：存放自定义的功能组件
    - **enums** : 定义访问API的账户类型，以枚举的形式
    - redprint : 自定义的红图类
  - **validators** : 验证器相关代码
    - **froms** : 验证客户端的合法性
- ginger : 入口文件



- 客户端验证器
  - 定义验证账号为必传项，且长度大于5小于32
  - 定义密码：值可为空
  - 账号类型：自定义验证器验证参数是否符合要求

```python
from wtforms import Form, StringField, IntegerField
from wtforms.validators import DataRequired, length
from app.libs.enums import ClientTypeEnum


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
```

#### 4-3 处理不同客户端注册的方案

- 客户端提交数据到服务端的两种方式
  - Form表单：一般用于网页内
  - Json数据：一般用于小程序、客户端

- 服务端接收数据的两种方式：

  1. request.json

     - 如果是json数据传入验证器，就需要用【关键字参数

       ```python
       form = ClientForm(data=data)
       ```

  2. Request.args.to_dict() 

#### 4-4 创建User模型

> 2019-02-25 16:49:08

- 引用高级编程的base模块
- 编写用户注册方法
- 编写用户模型

#### 4-5 完成客户端注册

> 2019-04-04 15:38:47

- 通过新建一个User的验证器，继承ClientForm的基础验证，然后添加一些新的个性化的验证

  - ```python
    # ginger/validators/forms.py
    class UserEmailForm(ClientForm):
        account = StringField(validators=[
            Email(message='invalidate email')
        ])
        secreat = StringField(validators=[
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
    ```

- 编写邮箱客户端验证私有方法

  - ```python
    # /Users/omega/Downloads/学习成长/编程语言/python/mooc_py/Python Flask构建可扩展的RESTful API/ginger/app/api/v1/user.py
    def __reister_user_by_email():
        form = UserEmailForm(data=request.json)
        if form.validate():
            User.register_by_email(form.nickname.data,
                                   form.account.data,
                                   form.secret.data)
    ```

- 完成注册的路由方法编写，通过字典枚举调用方法

  - ```python
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
        return 'success'
    ```

    

####4-6生成用户数据

> 2019-04-04 16:41:40

在secure文件内配置sqlalchemy的链接串。

- 运行程序访问用户注册：

  - ```
    127.0.0.1:5000/v1/client/register
    ```

- 通过postman抛送数据，在body.row选择json格式

  - ```json
    {
        "account": "666@qq.com",
        "secret": "123456",
        "type": 100,
        "nickname": "zhanghao"
    }
    ```


#### 4-7 自定义异常对象

> 2019-05-14 16:42:42

代码编写的报错信息，未能正常返回。

自定义编写继承HTTPException,返回自定义的错误。

```
app.libs.error_code
```

```python
# 注意此处要用werkzeug的库，而不是http.client

from werkzeug.exceptions import HTTPException


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
```

#### 4-8 浅谈异常返回的标准与重要性

> 2019-05-15 17:08:19

返回的信息种类：

1. 业务数据
2. 操作成功提示信息
3. 错误异常信息
   1. HTML格式
   2. JSON格式

#### 4-9 自定义APIException

> 2019-05-15 16:44:54

/ginger/app/libs/error.py

通过重写HTTPException的get_body和get_headers

返回自定义的JSON格式数据

#### 5-1 重写WTForms 一

> 2019-05-16 17:14:35

相当于二次开发flask，使得代码更加精简，功能更强

####5-2 重写WTForms 二

2019-05-27 11:44:23

接收抛送过来的JSON数据

校验数据的合法性，通过继承WTForms，然后新增一个校验并抛出异常的方法

抛出的异常方法通过继承自定义的APIException来实现

最早继承的还是from werkzeug.exceptions import HTTPException

```sql
    def validate_for_api(self):
        valid = super(BaseForm, self).validate()
        if not valid:
            # 调用form的validate的时候，所有的错误信息会存到errors这个属性里
            # 把报错的errors传入自定义的参数异常方法里
            # 通过此方法，把WTForms不抛出异常的特性，实现抛出异常
            print(self.errors)
            raise ParameterException(msg=self.errors)
```

#### 5-3 可以接受定义的复杂，但不能接受调用的复杂

> 2019-05-27 14:11:00

精简视图函数中每次实例化Form时，都要传入json

```
    data = request.json
    # 如果客户端传送的是json数据，传入数据到验证器则需要用【关键字参数】
    form = ClientForm(data=data)
```

```
# request.json的数据隐藏在了ClientForm的基类中直接调用，简化调用
    form = ClientForm()
```

两行精简成一行：

```
    form = ClientForm()
    form.validate_for_api()
```

```
    # 但是validate_for_api()需要返回form
form = ClientForm().validate_for_api()

```

- 定义的代码不管多复杂，都只是一次性的
- 调用是经常会用到的，所以越简单越好

#### 5-4 已知异常与未知异常

对异常信息进行处理

常见的异常类型：

- 已知异常：可以预知的异常
- 未知异常：未能料想到的异常

#### 5-5 全局异常处理

> 2019-05-27 16:46:36

通过全局异常处理，规范异常返回信息

```python
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
```

#### 6-1 Token概述

