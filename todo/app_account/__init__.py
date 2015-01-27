# -*- coding: utf-8 -*-
__author__ = 'florije'

from flask import Blueprint
from ..custom_api import Api

app_account = Blueprint('app_account', __name__)
api_account = Api(app_account, catch_all_404s=True)

from . import views

# api_account.add_resource(views.DemoHandler, '/demo')