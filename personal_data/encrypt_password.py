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
    password = hash_password(password)
    
    # Check if the password matches
    result = bcrypt.checkpw(password, hashed_password)
    
    return result
