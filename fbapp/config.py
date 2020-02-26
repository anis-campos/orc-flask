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
    FB_APP_ID = "489112975300358"
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://fbapp:fbapp@data:5432/fbapp'


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    # Active le debogueur
    DEBUG = True
    TESTING = True
    LIVESERVER_PORT = 8943
    LIVESERVER_TIMEOUT = 10

    # Facebook test user
    FB_USER_NAME = "Ellen"
    FB_USER_PW = "YOLOYOLO"
    FB_USER_EMAIL = "ellen_rmilrcp_page@tfbnw.net"
    FB_USER_ID = 100018814390853
    FB_USER_GENDER = 'female'

    QLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app_test.db')
