#!/usr/bin/python3
"""Main module for the AirBnB API v1."""

from flask import Flask, jsonify
from flask_cors import CORS
from models import storage
from api.v1.views import app_views
from os import getenv

app = Flask(__name__)

app.url_map.strict_slashes = False
app.register_blueprint(app_views)
CORS(app, origins=["0.0.0.0"])


@app.teardown_appcontext
def close_storage(exception):
    """Remove the current SQLAlchemy session"""
    storage.close()


@app.errorhandler(404)
def error_handler(error):
    return jsonify({"error": "Not found"}), 404


if __name__ == "__main__":
    host = getenv("HBNB_API_HOST", "0.0.0.0")
    port = int(getenv("HBNB_API_PORT", 5000))

    app.run(host, port, threaded=True, debug=True)
