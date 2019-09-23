# _*_ coding: UTF-8 _*_
# 开发团队  : 宽粉汇科
# 开发人员  : LianXiaoRui
# 开发时间  : 2019/9/19 16:01
# 文件名称  : __init__.py.py
# 开发工具  : PyCharm
# 项目名称  : westfield
from flask import Flask
from App.views import init_view


def create_app():
    app = Flask(__name__)
    init_view(app=app)

    return app