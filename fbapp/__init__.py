from . import models
from .views import app


@app.cli.command()
def init_db():
    models.init_db()
