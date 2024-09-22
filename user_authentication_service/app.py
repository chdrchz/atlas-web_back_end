#!/usr/bin/env python3

from auth import Auth
from flask import Flask, jsonify, request

app = Flask(__name__)

# Set the auth_type
AUTH = Auth()


@app.route('/',  methods=['GET'])
def hello():
    """ Generates a welcome message.
    """
    return jsonify({"message": "Bienvenue"})


@app.route('/users',  methods=['POST'])
def users():
    """ Finds the user based on email and password

    Args:
        email (_type_): Email for user
        password (_type_): Password for user

    Returns:
        200 or 400
    """
    email = request.form['email']
    password = request.form['password']
    try:
        AUTH.register_user(email, password)
        return jsonify({"email": email, "message": "user created"}), 200
    except ValueError:
        return jsonify({"message": "email already registered"}), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
