# -*- coding: utf-8 -*-
__author__ = 'boqingfu'

from . import db

from wtforms.validators import Email
from werkzeug.security import generate_password_hash, check_password_hash


class BaseModel(db.Model):
    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, unique=True)


class UserModel(BaseModel):
    __tablename__ = 'users'

    email = db.Column(db.String(120), unique=True, nullable=False, info={'validators': Email()})
    password = db.Column(db.String(80), nullable=False)

    def __init__(self, email, password):
        self.email = email
        self.password = generate_password_hash(password)

    def __repr__(self):
        return '<User %r>' % self.email

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)


class TaskModel(BaseModel):
    __tablename__ = 'tasks'

    title = db.Column(db.String(120), unique=True, nullable=False, default='')
    content = db.Column(db.String(120), unique=True, nullable=False, default='')

    def __init__(self, content, title):
        self.title = title
        self.content = content

    def __repr__(self):
        return '<Task %r>' % self.content