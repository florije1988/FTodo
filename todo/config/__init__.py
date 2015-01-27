# -*- coding: utf-8 -*-
__author__ = 'boqingfu'
import os
from .development import DevelopmentConfig
from .production import ProductionConfig
from .testing import TestingConfig


def load_config():
    """加载配置类"""
    mode = os.environ.get('MODE')
    try:
        if mode == 'PRODUCTION':
            from .production import ProductionConfig

            return ProductionConfig
        elif mode == 'TESTING':
            from .testing import TestingConfig

            return TestingConfig
        else:
            from .development import DevelopmentConfig

            return DevelopmentConfig
    except ImportError, e:
        from .default import Config

        return Config


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,

    'default': DevelopmentConfig
}