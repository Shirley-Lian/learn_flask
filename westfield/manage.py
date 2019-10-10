from flask_migrate import MigrateCommand
from flask_script import Manager
from App import create_app
import os
os.environ['FLASK_ENV'] = 'develop'

env = os.environ.get("FLASK_ENV") or 'default'
app = create_app(env)

manager = Manager(app=app)
# 添加数据库迁移指令
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
