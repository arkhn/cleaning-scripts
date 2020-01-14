from flask import Flask
from flask_cors import CORS
from app.config import Config

app = Flask(__name__)
CORS(
    app,
    origins=[
        r"^https?://.*\.?arkhn\.org(?::\d+)?$",
        r"^https?://.*\.?arkhn\.com(?::\d+)?$",
        r"^https?://.*\.?ark\.hn(?::\d+)?$",
        r"^https?://localhost(?::\d+)?$",
        r"^https?://0.0.0.0(?::\d+)?$",
    ],
)
app.config.from_object(Config)

from app import routes  # noqa
