# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 16:24:20 2020
Task Master Application.
@author: Deepesh W
"""

import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    #SECRET_KEY = 'this-really-needs-to-be-changed'
    MYSQL_DATABASE_HOST='localhost'
    MYSQL_DATABASE_PORT=3306
    MYSQL_DATABASE_USER='root'
    MYSQL_DATABASE_PASSWORD='romamw*9'
    MYSQL_DATABASE_DB='customers'

    MAIL_SERVER='smtp.gmail.com'
    MAIL_PORT=465
    MAIL_USERNAME='wadhwani.deep52@gmail.com'
    MAIL_PASSWORD= 'ugbshnwbkxvyvsxg'
    MAIL_USE_TLS=False
    MAIL_USE_SSL=True

   # SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']


class ProductionConfig(Config):
    DEBUG = False


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    TESTING = True