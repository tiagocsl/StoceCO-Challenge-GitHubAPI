# -*- coding: utf-8 -*-
import os


class Config:
    # --------------------#
    # Flask Configuration #
    # --------------------#
    DEBUG = False
    TESTING = False
    PORT = 5000

    # -----------#
    # redis main #
    # -----------#
    REDIS_HOST = "cache"  # docker network
    REDIS_PORT = 6379
    CHARSET = 'utf-8'
    DECODE_RESPONSES = True


class DevelopmentConfig(Config):

    ENV = os.environ.get("FLASK_ENV", "development")
    DEBUG = True
    ASSETS_DEBUG = True


class TestingConfig(Config):

    ENV = os.environ.get("FLASK_ENV", "testing")
    DEBUG = True
    TESTING = True


class ProductionConfig(Config):

    ENV = os.environ.get("FLASK_ENV", "production")
    DEBUG = False
    USE_RELOADER = False


settings = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig,
}