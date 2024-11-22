#!/usr/bin/env python3

from flask import Flask, jsonify
from api.v1.views import app_views

app = Flask(_name_)
app.register_blueprint(app_views)

@app.errorhandler(401)
def unauthorized_error_handler(error):
    return jsonify({"error": "Unauthorized"}), 401
