# -*- coding: utf-8 -*-
__author__ = 'florije'

import os

from flask.ext.script import Manager, Shell, Server
from flask.ext.migrate import Migrate, MigrateCommand

from todo import create_app
from todo.models import db


app = create_app(os.getenv('FLASK_CONFIG') or 'development')

manager = Manager(app)
manager.add_command("runserver", Server())
manager.add_command("shell", Shell())

migrate = Migrate(app, db)


def make_shell_context():
    # return dict(app=app, db=db, TaskModel=TodoModel)
    return dict(app=app)


manager.add_command("shell", Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)


@manager.command
def create_db():
    from todo import db

    db.create_all()


if __name__ == '__main__':
    manager.run()  # runserver -p 5000 -h 127.0.0.1