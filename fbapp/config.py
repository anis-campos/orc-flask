import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = '@@9\r!6Zr7\'"bt-=\nY\nBQ1A\rh'
    FB_APP_ID = "489112975300358"
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')


class ProductionConfig(Config):
    FB_APP_ID = "525369721720539"
    SQLALCHEMY_DATABASE_URI = 'postgresql:/data/fbapp'


class StagingConfig(Config):
    FB_APP_ID = "525369721720539"
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://fbapp:fbapp@data:5432/fbapp'


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
