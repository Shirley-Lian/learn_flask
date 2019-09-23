# _*_ coding: UTF-8 _*_
# 开发团队  : 宽粉汇科
# 开发人员  : LianXiaoRui
# 开发时间  : 2019/9/19 16:01
# 文件名称  : view.py
# 开发工具  : PyCharm
# 项目名称  : westfield
from App.views.second_blue import second
from .first_blue import first

# def init_route(app):
#     @app.route('/')
#     def hello_world():
#         a = 10
#         b = 6
#         c = 0
#         d = a+b/c
#         return 'Hello World!'


def init_view(app):
    # 注册蓝图
    app.register_blueprint(first)
    app.register_blueprint(second)