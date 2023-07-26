from flask import Flask

DATABASE_ENGINE='mysql'
DATABASE_HOST = 'localhost'
DEV_DATABASE_NAME='librarie-db-dev'
PROD_DATABASE_NAME='librarie-db-prod'
TEST_DATABASE_NAME='librarie-db-test'
SQLITE_DATABASE = 'local-db'
DATABASE_USERNAME ='root'
DATABASE_USER_PASSWORD = ''
DATABASE_PORT = '3306'
SQLITE_URI = f'sqlite:////tmp/{SQLITE_DATABASE}.db'

import secrets
# JWT_SECRET_KEY = secrets.token_hex(16)
JWT_SECRET_KEY = '5dd074d63e3116b2b03ee9dcd0ced4df'
print('KEY ==>', JWT_SECRET_KEY)


class Config(object):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI=f'{DATABASE_ENGINE}+pymysql://{DATABASE_USERNAME}:{DATABASE_USER_PASSWORD}@{PROD_DATABASE_NAME}:{DATABASE_PORT}/{DEV_DATABASE_NAME}'

class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = f'{DATABASE_ENGINE}+pymysql://{DATABASE_USERNAME}:{DATABASE_USER_PASSWORD}@{DATABASE_HOST}:{DATABASE_PORT}/{DEV_DATABASE_NAME}'
    DEBUG = True
    SQLALCHEMY_ECHO = False

class TestingConfig(Config):
    SQLALCHEMY_DATABASE_URI = f'{DATABASE_ENGINE}+pymysql://{DATABASE_USERNAME}:{DATABASE_USER_PASSWORD}@{DATABASE_HOST}:{DATABASE_PORT}/{TEST_DATABASE_NAME}'
    DEBUG = True
    SQLALCHEMY_ECHO = False

SECRET_VALUES = {
"SECRET_KEY" : secrets.token_hex(16),
"SECURITY_PASSWORD_SALT" :"Soçdy@m/9050@_#*-"
}

MAIL_SERVER="smtp.gmail.com"
# MAIL_USERNAME="yaomariussodokin@gmail.com"
# MAIL_PASSWORD="beagvuxewtwwutib"

MAIL_USERNAME="yaomariussodokin@gmail.com"
MAIL_PASSWORD="lwubrrlsefquxxlw"

MAIL_SUPPRESS_SEND = False
MAIL_DEBUG = True
MAIL_USE_TLS=True
MAIL_USE_SSL=False
MAIL_PORT=587
# MAIL_PORT=465
MAIL_DEFAULT_SENDER = MAIL_USERNAME


app = Flask(__name__)


MAIL_CONF = {
"MAIL_DEFAULT_SENDER" :"yaomariussodokin@gmail.com",
"MAIL_SERVER":"smtp.gmail.com",
"MAIL_USE_TLS":False,
"MAIL_USE_SSL":True,
"MAIL_PORT":587,
"MAIL_USERNAME":"yaomariussodokin@gmail.com",
"MAIL_PASSWORD":"lwubrrlsefquxxlw"
}
