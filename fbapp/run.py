from os import environ

from fbapp import create_app

if __name__ == "__main__":
    if environ.get('FLASK_ENV') is None:
        environ["FLASK_ENV"] = "development"
    create_app().run()
