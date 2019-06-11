from app.app import Flask


def register_blueprints(app):
    from app.api.v1 import create_blueprint_v1
    app.register_blueprint(create_blueprint_v1(), url_prefix='/v1')


def register_plugin(app):
    from app.models.base import db
    db.init_app(app)
    with app.app_context():
        # create_all()需要在上下文的环境中才能完成相关的操作
        db.create_all()


def create_app():
    """ 初始化核心对象和配置文件 """
    # 初始化核心对象
    app = Flask(__name__)

    # 加载配置文件
    app.config.from_object('app.config.setting')
    app.config.from_object('app.config.secure')

    # 注册蓝图
    register_blueprints(app)

    # 注册sqlalchemy
    register_plugin(app)

    return app
