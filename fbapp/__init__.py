from flask import Flask


def create_app() -> Flask:
    app = Flask(__name__)

    from . import config
    if app.config["ENV"] == "production":
        app.config.from_object(config.ProductionConfig)
    elif app.config["ENV"] == "staging":
        app.config.from_object(config.StagingConfig)
    elif app.config["ENV"] == "testing":
        app.config.from_object(config.TestingConfig)
    else:
        app.config.from_object(config.DevelopmentConfig)

    from .models import db
    db.init_app(app)

    from .views import frontend
    app.register_blueprint(frontend)

    return app
