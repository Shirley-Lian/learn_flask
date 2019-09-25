# _*_ coding: UTF-8 _*_
# 开发团队  : 宽粉汇科
# 开发人员  : LianXiaoRui
# 开发时间  : 2019/9/23 17:37
# 文件名称  : second_blue.py
# 开发工具  : PyCharm
# 项目名称  : westfield
from flask import Blueprint, redirect, url_for

second = Blueprint('second', __name__)


@second.route('/second/', methods=['GET', 'POST'])
def hello():
    return 'hello second'


@second.route('/getint/<int:id>')
def getint(id):
    print(id)
    print(type(id))
    return 'get id success'


@second.route('/redirect/')
def getredirect():
    # 重定向
    # return redirect('/hi/')
    # 反向解析
    return redirect(url_for('first.hi'))