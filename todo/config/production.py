# -*- coding: utf-8 -*-
__author__ = 'boqingfu'
from .default import Config


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = ''