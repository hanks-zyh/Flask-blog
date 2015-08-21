#!/usr/bin/env python3
# -*- coding:utf-8 -*-

__author__ = 'Hanks'

import os
from app import create_app, db
from app.models import User, Role, Post
from flask.ext.script import Manager, Shell
from flask.ext.migrate import Migrate, MigrateCommand

COV = None
if os.environ.get('FLASK_COVERAGE'):
    import coverage

    COV = coverage.coverage(branch=True, include='app/*')
    COV.start()

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)
migrate = Migrate(app, db)


def make_shell_context():
    return dict(app=app, db=db, User=User, Role=Role, Post=Post)


manager.add_command("shell", Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)


@manager.command
def test(coverage=False):
    """Run the unit tests."""
    if coverage and not os.environ.get('FLASK_COVERAGE'):
        import sys
        os.environ['FLASK_COVERAGE'] = '1'
        os.execvp(sys.executable, [sys.executable] + sys.argv)
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)
    if COV:
        COV.stop()
        COV.save()
        print('Coverage Summary:')
        COV.report()
        basedir = os.path.abspath(os.path.dirname(__file__))
        covdir = os.path.join(basedir, 'tmp/coverage')
        COV.html_report('HTML version: file://%s/index,html' % covdir)
        COV.erase()


@manager.command
def deploy():
    """ Run deploy tasks."""
    from flask.ext.migrate import upgrade
    from  app.models import Role, User
    # 把数据库迁移
    upgrade
    # 创建用户角色
    Role.insert_roles()
    # 让所有用户关注自己
    User.add_self_follows()


if __name__ == '__main__':
    manager.run()
