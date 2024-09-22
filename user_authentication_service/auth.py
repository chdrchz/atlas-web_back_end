#!/usr/bin/env python3
""" Module that contains an Auth class to authenticate
    user objects.

    Functions:
        - def register_user(self, email: str, password: str
            ) -> User:
                - Method that checks if a user exists, and if not,
                adds to database

    Other functions:
        - def _hash_password(password: str) -> bytes:
                - Method that salts and hashes a password
"""

import bcrypt
from db import DB
from user import User
from sqlalchemy.exc import NoResultFound


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
        try:

            # Try to find the User based on email
            user = self._db.find_user_by(email=email)
            raise ValueError(f"User {email} already exists")  # User found

        except NoResultFound:

            # Hash the password
            hashed_password = _hash_password(password)

            # Save the User to the database with hashed password
            user = self._db.add_user(email, hashed_password)
            return user

    def valid_login(self, email, password) -> bool:
        """ Method that verifies passwords match

        Args:
            email (_type_): Email for user
            password (_type_): password for user

        Returns:
            bool: _description_
        """
        # Try to find the user
        user = self._db.find_user_by(email=email)
        if user:
            hashed_password = _hash_password(password)

            # Are the passwords the same?
            if bcrypt.checkpw(password, hashed_password):
                return True
            else:
                return False


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
