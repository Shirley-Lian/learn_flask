# _*_ coding: UTF-8 _*_
# 开发团队  : 宽粉汇科
# 开发人员  : LianXiaoRui
# 开发时间  : 2019/9/19 16:20
# 文件名称  : first_blue.py
# 开发工具  : PyCharm
# 项目名称  : westfield
from flask import Blueprint, render_template

first = Blueprint("first", __name__)


@first.route('/hi/')
def hi():
    return render_template('index.html', msg='lianxiaorui')