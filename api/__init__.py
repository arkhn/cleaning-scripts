from flask import Flask

from api.config import Config
from api.routes import api


def create_app():
    app = Flask(__name__)
    app.register_blueprint(api)
    app.config.from_object(Config)
    return app


app = create_app()
