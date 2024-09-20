#!/usr/bin/env python3
""" Module of session auth views
"""

import os
from models.user import User
from api.v1.views import app_views
from flask import abort, jsonify, make_response, request


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def login() -> str:
    """_summary_

    Returns:
        str: _description_
    """
    # Get the email and password
    email = request.form.get('email')
    password = request.form.get('password')
    
    # If the email is valid, find the user
    if email:
        users = User.search({"email": email})
        if users:
            
            user = users[0]
            # If the User exists, try to authenticate the password
            if not user.is_valid_password(password):
                return jsonify({"error": "wrong password"}), 400

            # The user is authenticated with password, create a session
            else:
                from api.v1.app import auth
                
                # Create the session
                session_id = auth.create_session(user.id)
                
                # Grab that data from User
                response = make_response(user.to_json())
                
                # Set the cookie for the user
                response.set_cookie(os.getenv(
                    'SESSION_NAME', '_my_session_id'), session_id)
                return response
        
        # User was not found
        else:
            return jsonify({"error": "no user found for this email"}), 404   

    # Email was not found
    else:
        return jsonify({"error": "email missing"}), 400
