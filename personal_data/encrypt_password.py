#!/usr/bin/env python3
""" Module that contains a function to
    hash + salt passwords
"""

import bcrypt


def hash_password(password: str) -> bytes:
    """ Function that hashes and salts a password
    """
    bytes = password.encode('utf-8')

    salt = bcrypt.gensalt()

    hash = bcrypt.hashpw(bytes, salt)

    return hash
