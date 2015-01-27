# -*- coding: utf-8 -*-
__author__ = 'boqingfu'
from .default import Config
import os


class DevelopmentConfig(Config):
    # DEBUG = True
    # SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or 'sqlite:///' + os.path.join(basedir,
    #                                                                                             'data-dev.sqlite')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or 'mysql://user:password@ip/database'