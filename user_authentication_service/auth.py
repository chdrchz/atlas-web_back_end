#!/usr/bin/env python3

import bcrypt


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
