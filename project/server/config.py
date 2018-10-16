# project/server/config.py

import os

basedir = os.path.abspath(os.path.dirname(__file__))


class BaseConfig(object):
    """Base configuration."""
    APP_NAME = os.getenv('APP_NAME', 'Flask Skeleton')
    BCRYPT_LOG_ROUNDS = 4
    DEBUG_TB_ENABLED = False
    SECRET_KEY = os.getenv('SECRET_KEY', 'my_precious')
    WTF_CSRF_ENABLED = False
    APP_ADMIN_TOKEN = 'YOUR-SECRET-ADMIN-KEY'


class DevelopmentConfig(BaseConfig):
    """Development configuration."""
    DEBUG_TB_ENABLED = True
    DEBUG_TB_INTERCEPT_REDIRECTS = False


class TestingConfig(BaseConfig):
    """Testing configuration."""
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    TESTING = True
    APP_PROVIDER = "test"


class ProductionConfig(BaseConfig):
    """Production configuration."""
    BCRYPT_LOG_ROUNDS = 13
    WTF_CSRF_ENABLED = True
