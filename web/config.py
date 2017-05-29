import os
from configparser import ConfigParser

basedir = os.path.abspath(os.path.dirname(__file__))


def secure_config(cls):
    """
    Adds a settings which should be kept secure.
    """
    config_parser = ConfigParser()
    configuration_directory = os.path.dirname(__file__)
    secure_path = os.path.join(configuration_directory, 'secure_config.ini')
    if secure_path:
        config_parser.read(secure_path)
        secret_key = config_parser['db']['secret_key']
        mail_password = config_parser['mail']['password']
        setattr(cls, "SECRET_KEY", secret_key)
        setattr(cls, "MAIL_PASSWORD", mail_password)
    return cls


# -------------------------------------------
# Configuration for flask and its extensions
# -------------------------------------------
@secure_config
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
    # USER_AFTER_LOGIN_ENDPOINT = 'main.index'   # TODO change this
    # USER_AFTER_LOGOUT_ENDPOINT = 'main.logout_screen'  # TODO change this


class DevelopmentConfig(Config):
    DEBUG = True


class ProductionConfig(Config):
    pass


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite://'


def create_configuration(configuration_type=None):
    """
    Creates a configuration for flask to set up itself and the extensions. The
    configuration can be either DevelopmentConfig, ProductionConfig or TestingConfig.
    
    :param configuration_type: The type of configuration as a string
    :return: a configuration class
    """
    config = {'development': DevelopmentConfig,
              'production': ProductionConfig,
              'testing': TestingConfig}

    if configuration_type is None:
        configuration_name = os.environ.get('COLAB_CONFIG', 'production')
        return config[configuration_name]
    elif configuration_type in config:
        return config[configuration_type]
    else:
        raise ValueError("The colab configuration {} is not known. "
                         "Please select production, development or testing or"
                         " set up the appropriate environment variable".format(configuration_type))
