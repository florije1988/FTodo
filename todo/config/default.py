# -*- coding: utf-8 -*-
__author__ = 'boqingfu'


class Config:
    def __init__(self):
        pass

    DEBUG = False
    TESTING = False

    SQLALCHEMY_ECHO = True
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True

    APP_DEBUG = True
    HOST = 'localhost'
    PORT = 5000
    LOG_PATH = 'logs'
    LOG_NAME = 'proj_logs.log'

    @staticmethod
    def init_app(app):
        pass