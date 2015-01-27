# -*- coding: utf-8 -*-
__author__ = 'boqingfu'
from .default import Config


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = ''