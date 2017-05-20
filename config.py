import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    DEBUG = False
    TESTING = False
    # ----------------
    # App settings
    # ----------------
    APP_NAME = "CoLab Chat App"
    APP_SYSTEM_ERROR_SUBJECT_LINE = APP_NAME + " system error"

    # ----------------
    # General
    # ----------------
    SECRET_KEY = '\xcf\xffo\xc3\xc8A\x88\xa8\x8a\xd8\xe1\xdd\xab\xeay-\xda\xfe\x14\x1bR\xc3\xd2g' # TODO make this local
    CSRF_ENABLED = True

    # ----------------
    # SQL Alchemy
    # ----------------
    SQLALCHEMY_DATABASE_URI = 'sqlite:///../colab_server.sqlite'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # -------------------
    # Flask Mail
    # -------------------
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_SSL = False
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'colab.chat.app@gmail.com'
    MAIL_PASSWORD = 'A$amHack2017'
    MAIL_DEFAULT_SENDER = '"CoLab Chat" <colab.chat.app@gmail.com>'

    ADMINS = [
        '"Admin One" <colab.chat.app@gmail.com>',
    ]

    # ---------------------
    # WTF
    # ---------------------
    WTF_CSRF_ENABLED = True

    # ---------------------
    # Flask User
    # --------------------
    USER_APP_NAME = APP_NAME
    USER_ENABLE_CHANGE_PASSWORD = True
    USER_ENABLE_CHANGE_USERNAME = False
    USER_ENABLE_CONFIRM_EMAIL = True
    USER_ENABLE_FORGOT_PASSWORD = True
    USER_ENABLE_EMAIL = True
    USER_ENABLE_REGISTRATION = True
    USER_ENABLE_RETYPE_PASSWORD = True
    USER_ENABLE_USERNAME = False
    #USER_AFTER_LOGIN_ENDPOINT = 'main.index'   # TODO change this
    #USER_AFTER_LOGOUT_ENDPOINT = 'main.logout_screen'  # TODO change this


class DevelopmentConfig(Config):
    DEBUG = True


class ProductionConfig(Config):
    pass


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite://'


config = {'development': DevelopmentConfig,
          'production': ProductionConfig,
          'testing': TestingConfig}
