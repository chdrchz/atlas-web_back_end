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

    # Season and hash the password
    return bcrypt.hashpw(password, salt)
