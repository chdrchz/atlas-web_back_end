#!/usr/bin/env python3
""" Module that hashes and salts passwords,
    and checks against them to verify login state

    Functions:
        - hash_password():
            hashes and salts a string (password)
        - is_valid():
            returns a boolean if the hashed passwords match
"""

import bcrypt


def hash_password(password: str) -> bytes:
    """ Function that hashes and salts a password

        Args:
            - password: the password to hash and salt

        Return:
            - hashed + salted password in bytes
    """
    bytes = password.encode('utf-8')

    salt = bcrypt.gensalt()

    hash = bcrypt.hashpw(bytes, salt)

    return hash


def is_valid(hashed_password: bytes, password: str) -> bool:
    """ Function that checks if a password
        matches a hashed password

        Args:
            - hashed_password: the hashed password from hash_password()
            - password: the password to be checked against

        Return:
            - Boolean:
                - True if the password matches the hashed_password
                - False if the password doesn't match the hashed_password
    """
    # First of all, hash that pass!
    password_bytes = password.encode('utf-8')

    # Check if the password matches
    result = bcrypt.checkpw(password_bytes, hashed_password)

    return result
