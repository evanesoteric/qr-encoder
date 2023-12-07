from os import environ

from dotenv import load_dotenv
load_dotenv()



class Config:
    DEBUG = False
    TESTING = False
    SECRET_KEY = environ.get('SECRET_KEY')
    APP_NAME = environ.get('APP_NAME')

class DevelopmentConfig(Config):
    DEBUG = True
    TESTING = False

class ProductionConfig(Config):
    DEBUG = False
    TESTING = False

class TestingConfig(Config):
    DEBUG = False
    TESTING = True

