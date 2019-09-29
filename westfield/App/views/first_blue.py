# _*_ coding: UTF-8 _*_
# 开发团队  : 宽粉汇科
# 开发人员  : LianXiaoRui
# 开发时间  : 2019/9/19 16:20
# 文件名称  : first_blue.py
# 开发工具  : PyCharm
# 项目名称  : westfield
from flask import Blueprint, render_template

from App.ext import db
from App.models import User

first = Blueprint("first", __name__)


@first.route('/hi/')
def hi():
    return render_template('hello.html', msg='lianxiaorui')


@first.route('/createdb/')
def createdb():
    db.create_all()
    return '添加表成功'


@first.route('/dropdb/')
def dropdb():
    db.drop_all()
    return '删除成功'


@first.route('/adddata/')
def add_user():
    user = User()
    user.username = 'tom'
    user.save()
    return '添加数据成功'