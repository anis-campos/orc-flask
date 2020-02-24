import os

SECRET_KEY = '@@9\r!6Zr7\'"bt-=\nY\nBQ1A\rh'
FB_API_ID = "525369721720539"

basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
