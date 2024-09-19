#!/usr/bin/env python3
""" Route module for the API

    Functions:
        - before_request_handler(): Runs before everythign else,
            and handles authorizing paths
        - def not_found(error) -> str: Throws a 404 error
        - def unauthorized(error) -> str: Throws a 401 error
        - def forbidden(error) -> str: Throws a 403 error
"""
from os import getenv
from api.v1.auth.auth import Auth
from api.v1.views import app_views
from flask import Flask, jsonify, abort, request
from flask_cors import (CORS, cross_origin)
import os

app = Flask(__name__)
app.register_blueprint(app_views, url_prefix='/api/v1')
CORS(app, resources={r"/api/v1/*": {"origins": "*"}})

# Initialize auth variable
auth = None

# Check environment variable and configure authentication
# based on auth_type
auth_type = os.getenv('AUTH_TYPE')

if auth_type == "basic_auth":
    from api.v1.auth.basic_auth import BasicAuth
    auth = BasicAuth()
else:
    auth = Auth()


@app.before_request
def before_request_handler():
    """ Authorizing access based on paths
    """
    if auth is None:
        return

    # No authentication needed for these
    excluded_paths = [
        '/api/v1/status/',
        '/api/v1/unauthorized/',
        '/api/v1/forbidden/'
    ]

    # Is the path in public paths?
    if request.path in excluded_paths:
        return

    # Do auth stuff
    if request.path not in excluded_paths and \
            auth.require_auth(request.path, excluded_paths):
        if auth.authorization_header(request) is None:
            abort(401)  # Unauthorized
    
    request.current_user = auth.current_user(request)


@app.errorhandler(404)
def not_found(error) -> str:
    """ Not found handler
    """
    return jsonify({"error": "Not found"}), 404


@app.errorhandler(401)
def unauthorized(error) -> str:
    """ Not authorized handler
    """
    return jsonify({"error": "Unauthorized"}), 401


@app.errorhandler(403)
def forbidden(error) -> str:
    """ Forbidden handler
    """
    return jsonify({"error": "Forbidden"}), 403


if __name__ == "__main__":
    host = getenv("API_HOST", "0.0.0.0")
    port = getenv("API_PORT", "5000")
    app.run(host=host, port=port)
