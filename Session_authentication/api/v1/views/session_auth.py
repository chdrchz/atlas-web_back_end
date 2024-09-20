#!/usr/bin/env python3
""" Module of session auth views
"""

import os
from api.v1.auth import auth
from models.user import User
from api.v1.views import app_views
from flask import abort, jsonify, make_response, request


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def login() -> str:
    """ Function that handles the whole prcoess of authenticating,
        and creating a session based on a user

    Returns:
        str: response data
    """
    # Get the email and password from the request form
    email = request.form.get('email')
    password = request.form.get('password')

    # Check if the email is provided
    if not email:
        return jsonify({"error": "email missing"}), 400

    # Check if the password is provided
    if not password:
        return jsonify({"error": "password missing"}), 400

    # Search for the user with the given email
    users = User.search({"email": email})

    # If no users are found, return a 404 error
    if not users or len(users) == 0:
        return jsonify({"error": "no user found for this email"}), 404

    # Assuming there's at least one user, take the first user
    user = users[0]

    # Check if the password is valid
    if not user.is_valid_password(password):
        return jsonify({"error": "wrong password"}), 401

    # The user is authenticated, create a session
    from api.v1.app import auth
    session_id = auth.create_session(user.id)

    # Generate the response with the user info and set the session cookie
    response = make_response(user.to_json())
    response.set_cookie(os.getenv(
            'SESSION_NAME', '_my_session_id'), session_id)

    return response


@app_views.route('/api/v1/auth_session/logout', methods=['DELETE'], strict_slashes=False)
def logout() -> str:
    """ Method that logs the user out

    Returns:
        str: jsonify({}), 200
    """
    if not auth.destroy_session(request):
        abort(404)
    return jsonify({}), 200
