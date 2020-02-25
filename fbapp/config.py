import os

SECRET_KEY = '@@9\r!6Zr7\'"bt-=\nY\nBQ1A\rh'
FB_APP_ID = "489112975300358"

basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
