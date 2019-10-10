# _*_ coding: UTF-8 _*_
# 开发团队  : 宽粉汇科
# 开发人员  : LianXiaoRui
# 开发时间  : 2019/9/24 15:15
# 文件名称  : ext.py
# 开发工具  : PyCharm
# 项目名称  : westfield
# 初始化第三方扩展库
from flask_migrate import Migrate
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap

db = SQLAlchemy()
migrate = Migrate()


def init_ext(app):
    db.init_app(app=app)
    migrate.init_app(app=app, db=db)
    Session(app)
    Bootstrap(app)