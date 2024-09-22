#!/usr/bin/env python3
""" Module that contains an Auth class to authenticate
    user objects.

    Functions:
    
    Other functions:
        - def _hash_password(password: str) -> bytes:
                - Method that salts and hashes a password
"""

import bcrypt
from db import DB
from user import User


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """ Method that checks if a user exists and if not,
            adds them to the database

        Args:
            email (str): Email for user
            password (str): Password for user

        Returns:
            User: New User object
        """
        # Find the User based on email
        user = self._db.find_user_by(email=email)
        if user:
            raise ValueError(f"User {email} already exists")
        else:
            # Hash the password
            hashed_password = _hash_password(password)
            
            # Save the User to the databse w/ hashed pass
            user = self._db.add_user(email, hashed_password)
            return user

def _hash_password(password: str) -> bytes:
    """ Method that salts and hashes a password

    Args:
        password (str): Password to be salted and hashed

    Returns:
        bytes: Salted and hashed password
    """

    # Get the salt
    salt = bcrypt.gensalt()

    # Encode the password to bytes
    password_bytes = password.encode('utf-8')

    # Season and hash the password
    return bcrypt.hashpw(password_bytes, salt)
