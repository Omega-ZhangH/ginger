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

#### 3-2 为什么标准REST不适合内部开发

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

    

#### 4-6生成用户数据

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

> 2019-05-27 16:57:34

Token：令牌。

作用类似于浏览器在发送了用户名、密码给后端校验后，把票据写入到cookie.

- 有效期
- 可标识用户身份
- 令牌本身是加密的

#### 6-2 获取Token令牌

> 2019-05-28 11:21:25

在api的实现过程中获取令牌，既相当于在浏览器上设置cookie

- 需要实现用户的账号和密码校验
- 校验成功后需要有一个生成Token的方法
- 生成成功返回一个加密后的Token和Http状态码

```python

@api.route('', methods=['POST'])
# 之所以用POST方法是为了隐藏用户名密码，可以放在BODY中传.传参更安全
def get_token():
    """
    :return: 返回加密后的Token和一个HTTP状态码
    """
    # api的get_token就相当于web的login
    # 接收用户的参数
    form = ClientForm().validate_for_api()

    promise = {
        ClientTypeEnum.USER_EMAIL: User.verify
    }

    identity = promise[ClientTypeEnum(form.type.data)](
        form.account.data,
        form.secret.data
    )

    # 生成Token
    token = generate_auth_token(identity['uid'],
                                form.type.data,
                                expiration=current_app.config['TOKEN_EXPIRATION'])
    # 将Token字节码转换为ascii码
    t = {
        'token': token.decode('ascii')
    }

    return jsonify(t), 201


def generate_auth_token(uid, ac_type, scope=None, expiration=7200):
    """
    生成Token
    :param uid: 用户ID
    :param ac_type: 账户类型
    :param scope: 权限作用域
    :param expiration: 有效时间
    :return: 返回加密后的Token
    """
    s = Serializer(current_app.config['SECRET_KEY'],
                   expiration=expiration)
    return s.dumps({
        'uid': uid,
        'type': ac_type.value
    })
```

#### 6-3 Token的用处

- 用来标识用户的身份
- 需要校验Token的合法性和有效性
- 避免了用户访问不同页面频繁的输入账号和密码

#### 6-4 @auth拦截器执行流程

通过HTTPBasicAuth，来实现权限的校验和控制。

自定义一个校验装饰器，来进行保护

```python

from flask_httpauth import HTTPBasicAuth

auth = HTTPBasicAuth()


@auth.verify_password
def verify_password(account, paaword):
    pass

```

#### 6-5 HTTPBasicAuth基本原理

HTTPBasicAuth本身支持在header里面发送账号和密码

以键值对的形式展现：

key='Authorization'

账号密码是以basic+空格+base64加密后的字符串为消息传递

value=basic base64(账号:密码)

#### 6-6 以BasicAuth的方式发送Token

通过postman的Authorization选择basic Auth 在用户名里填写token的值

这样就避免了要转换成base64才能发送的问题

#### 6-7 验证Token

通过调用现有的库，实现token的序列化、和有效性和时效性的验证

同时用到小技巧namedtuple，返回一个对象

```python3
from collections import namedtuple

from flask import current_app, g
from flask_httpauth import HTTPBasicAuth
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer, BadSignature, SignatureExpired

from app.libs.error_code import AuthFailed

auth = HTTPBasicAuth()
User = namedtuple('User', ['uid', 'ac_type', 'scope'])


@auth.verify_password
def verify_password(token, paaword):
    user_info = verify_auth_token(token)
    # 如果认证失败的话
    if not user_info:
        return False
    else:
        g.user = user_info
        return True


def verify_auth_token(token):
    # 验证token是否合法
    s = Serializer(current_app.config['SECRET_KEY'])
    try:
        # 载入token
        data = s.loads(token)
    except BadSignature:
        raise AuthFailed(msg='token is invalid',
                         error_code=1002)
    except SignatureExpired:
        raise AuthFailed(msg='token was expired',
                         error_code=1003)
    uid = data['uid']
    ac_type = data['type']
    # 返回结果以对象式的形式返回
    return User(uid, ac_type, '')
```

#### 6-8 重写first_or_404与get_or_404

> 2019-05-29 09:51:29

获取用户信息的视图函数中要返回查询的用户信息。如果用户信息没找到，又要单独写一个raise



可以通过重写first_or_404和get_or_404来解决这个问题

```python
def get_or_404(self, ident):
    """
    重写BaseQuery中的方法，来实现自定义的报错返回
    :param ident:
    :return:
    """

    rv = self.get(ident)
    if rv is None:
        raise NotFound()
    return rv
```



#### 7-1 追求更好的写法

返回业务数据信息，在一个模型中，不能直接返回模型。需要转为字典模式，然后再json格式化返回出去

- 提高变成思维
- 抽象思维的能力
- 防止厌倦写代码
- 不只是追求功能的实现

#### 7-2 理解序列化时的default函数

jsonify在返回序列化数据时，如果flask知道怎么序列化就不会调用default函数

如果不知道怎么序列化时，就会调用default的函数，根据条件判断其中不同格式数据的

序列化方法

#### 7-3 不完美的对象转字典

对象的.\__dict__中

数据不会存放**类变量**，

但是会存放**实例变量**

```
class Name:

	name = '1'

	age = 2

def __init__(self):

		self.gender = 1

则Name对象实例化后
name=Name()
name.__dict__的值只是{"gender":1}
```

#### 7-4 深入理解dict的机制

当有\__getitem__方法时，实例化后的对象则可以像访问字典一样，访问对应的属性

```python
class Name(object):

    scope = 1
    age = 18

    def __init__(self):
        self.gender = 'male'

    def __getitem__(self, item):
        return getattr(self, item)

x = Name()
print(x['gender']) # male
```

当dict传入的值时对象的话，会读取类中的方法**keys**的类

```Python
class Name(object):

    scope = 1
    age = 18

    def __init__(self):
        self.gender = 'male'

    def keys(self):
        return ('age', 'gender')
    
    def __getitem__(self, item):
        return getattr(self, item)

print(dict(x))
```

#### 7-5 一个元素的元组要特别注意

keys方法如果想只返回一个元素的话，需要注意一个元素的元组需要加逗号

如：('age',);否则会报错，它会从第一个字母去解析

更简单的办法时返回的时候用**列表['gender']**，则不用加逗号，或者**集合set{'gender'}**

```
class Name(object):

    scope = 1
    age = 18

    def __init__(self):
        self.gender = 'male'

    def keys(self):
        return ('age',)
        # return ['age'] # 列表
				# return {'age'} # 集合
    
    def __getitem__(self, item):
        return getattr(self, item)

print(dict(x))
```

#### 7-6 序列化SQLAlchemy模型

在模型定义中添加**keys和\__getitem__**方法,控制模型的序列化

```python
class User(Base):
    id = Column(Integer, primary_key=True)
    email = Column(String(24), unique=True, nullable=False)
    nickname = Column(String(24), unique=True)
    # 权限标识:1、普通用户，2、管理员
    auth = Column(SmallInteger, default=1)
    #
    _password = Column('password', String(100))

    # 定义keys，__getattr__ 进行模型序列化时的属性控制
    def keys(self):
        return ['id', 'email', 'nickname', 'auth']

    def __getitem__(self, item):
        return getattr(self, item)
```

#### 7-7 完善序列化

> 2019-06-04 16:29:14

每个模型序列化都需要有keys和\__getitem__。为了简化代码，可以把\__getitem__放到基类中

如果模型中有时间格式的数据，则需要在default的下面加入判断条件

```python
        #处理时间类型的数据
        if isinstance(o, date):
            return o.strftime('%Y-%m-%d')
```

#### 7-8 ViewModel对于API有意义吗?

**ViewModel**是为视图层提供个性化的视图模型

- 可以个性化模型的返回值
- 可以处理一批的模型
- 可以合并不同的模型
- 但对于RESTful的规范，有没有ViewModel其实不太重要

#### 8-1 删除模型注意事项

> 2019-06-11 16:30:30

删除的时候调用的是DELETE。

实现方式是软删除，通过改变status的状态来实现

```python
# 删除用户的操作
@api.route('/<int:uid>', methods=['DELETE'])
@auth.login_required
def delete_user(uid):
    with db.auto_commit():
        # 直接调用get_or_404会能反复查询到想要的数据
        # user = User.query.get_or_404(uid)
        # filter_by方法会添加status=1的条件
        user = User.query.filter_by(id=uid).first_or_404()
        user.delete()
    return DeleteSuccess()
    
# 在user模型中定义的方法
def delete(self):
        # 软删除
        self.status = 0
```

#### 8-2 g变量中读取uid防止超权

通过flask的g变量来获取用户的uid

```python
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
```

#### 8-3 生成超级管理员账号

```python3
from app.models.base import db
from app.models.user import User
from app import create_app

app = create_app()

# 推入上下文
with app.app_context():
    with db.auto_commit():
        user = User()
        user.nickname = 'Super'
        user.auth = 2
        user.email = '999@qq.com'
        user.password = '123456'
        db.session.add(user)

```

#### 8-4 不太好的权限管理方案

> 2019-06-12 10:54:47

方案：

- 通过在生成token的时候加入身份标识is_admin 也就是scope
- 然后在解析token时解析出is_admin，从而判断是否是管理员

不太好的原因：

- 每个视图函数中都要写判断是否是超级管理员
- 如果一个项目中不只有普通用户和管理员的话，权限判断就会复杂
- 不够灵活和普适性更加复杂的权限管理

#### 8-5 比较好的权限管理方案

实现方式：

- 通过身份标识，编写对应的权限，在数据库表中
- 编写对应权限在redis中
- 编写对应权限在可配置文件中



#### 8-6 实现Scope权限管理 一

> 2019-06-18 11:34:59

通过在生产Token中写入scope的值是AdminScope 和UserScope

新建/ginger/app/libs/scope.py.编写定义权限作用域和判断

```python

# 定义管理员可访问的视图列表
class AdminScope:
    allow_api = ['super_get_user']


# 定义普通用户可访问的视图列表
class UserScope:
    allow_api = []


def is_in_scope(scope, endpoint):
    '''
    :param scope (str):传入解析toKen中的scope的值
    :param endpoint: 视图函数的目录
    '''
    if endpoint in scope.allow_api:
        return True
    else:
        return False
```

如果用户权限不够，则在认证用户Token的时候抛出异常

```python
    # 如果用户的权限不够则吗，返回认证失败
    allow = is_in_scope(scope, request.endpoint)
    if not allow:
        raise Forbidden()
```



#### 8-7 globals()实现“反射”

通过一个**类的名字**而得到一个**类的对象**：

- globals()方法会把当前文件中所有的变量和类变成一个字典

- 然后通过关键字，调用这个字典既可以得到一个

```python
def is_in_scope(scope, endpoint):
    '''
    :param scope (str):传入解析toKen中的scope的值
    :param endpoint: 视图函数的目录
    '''
    # 通过一个类的名字而得到一个类的对象：
    gl = globals()
    scope = globals()[scope]()

    if endpoint in scope.allow_api:
        return True
    else:
        return False
```

#### 8-8 实现Scope权限管理 二

因为我们的视图函数是建立在蓝图上的，所以endpoint是v1.get_super_user

```python

# 定义管理员可访问的视图列表
class AdminScope:
    allow_api = ['v1.super_get_user', 'v1.get_user']
    
```

#### 8-9 Scope优化一 支持权限相加

```python
# 定义管理员可访问的视图列表
class AdminScope:
    allow_api = ['v1.super_get_user', 'v1.get_user']
    # 权限相加
    def __init__(self):
        self.add(UserScope())

    def add(self, other):
        self.allow_api = self.allow_api + other.allow_api
```

#### 8-10 Scope优化 二 支持权限链式相加

通过在add函数中把自身返回回去，实现链式加权

```python
class AdminScope:
    allow_api = ['v1.super_get_user', 'v1.get_user']
    # 权限相加
    def __init__(self):
        self.add(UserScope()).add(SuperScope())

    def add(self, other):
        self.allow_api = self.allow_api + other.allow_api
				return self
```

#### 8-11 Scope优化 三 所有子类支持相加

通过继承一个基类，使得新定义的类能够支持权限相加

```python
# 定义一个基类，让权限相加的操作都能支持
class Scope:
    def add(self, other):
        self.allow_api = self.allow_api + other.allow_api
        return self
```

#### 8-12 Scope优化 四 运算符重载

实现对象的相加操作，需要用到运算符重载

```python
# 定义一个基类，让权限相加的操作都能支持
class Scope:
    # def add(self, other):
    def __add__(self, other):
        # 运算符重载，支持对象的相加
        self.allow_api = self.allow_api + other.allow_api
        return self
```

#### 8-13 Scope 优化 探讨模块级别的Scope

思路：通过指定视图函数所在的文件，读取其中的全量视图

将endpoint从v1+viewfunc 修改为 v1.redname + viewfunc

#### 8-14 Scope优化 实现模块级别的Scope

通过修改红图中的endpoint的格式来实现

```python
        for f, rule, options in self.mound:
            # options是字典，pop是删除如果有endpoint的key，返回对应的值，否则返回默认值
            # endpoint = options.pop("endpoint", f.__name__)
            # 修改endpoint的格式，变成：红图名字+视图名字
            endpoint = self.name + '+' + options.pop("endpoint", f.__name__)
            blueprint.add_url_rule(url_prefix + rule, endpoint, f, **options)

```

#### 8-15 Scope优化 七 支持排除

