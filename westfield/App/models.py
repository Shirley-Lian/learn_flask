# _*_ coding: UTF-8 _*_
# 开发团队  : 宽粉汇科
# 开发人员  : LianXiaoRui
# 开发时间  : 2019/9/24 14:56
# 文件名称  : models.py
# 开发工具  : PyCharm
# 项目名称  : westfield
from App.ext import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(16))

    # 添加数据
    def save(self):
        db.session.add(self)
        db.session.commit()