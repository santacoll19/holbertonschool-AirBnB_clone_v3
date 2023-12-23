#!/usr/bin/python3
"""start the Api"""
from flask import Flask
from models import storage
from api.v1.views import app_views
from flask import jsonify
from flask import Blueprint
from flask_cors import CORS
import os


app = Flask(__name__)
app.register_blueprint(app_views)
CORS(app, resources={r"/*": {"origins": "0.0.0.0"}})


@app.teardown_appcontext
def teardown(self):
    """Close storage"""
    storage.close()


@app.errorhandler(404)
def not_found(error):
    """Return error message"""
    return jsonify({"error": "Not found"}), 404


if __name__ == "__main__":
    HBNB_API_HOST = os.getenv('HBNB_API_HOST', default='0.0.0.0')
    HBNB_API_PORT = os.getenv('HBNB_API_PORT', default='5000')
    app.run(host=HBNB_API_HOST, port=HBNB_API_PORT, threaded=True)
