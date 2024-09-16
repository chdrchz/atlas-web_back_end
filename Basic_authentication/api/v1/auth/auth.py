#!/usr/bin/env python3
""" Auth module
"""

from flask import request
from typing import List, TypeVar

# Define a TypeVar for User
User = TypeVar('User')


class Auth():
    """ Template class for all authentication systems.
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        This method will later handle path authentication.
        Currently, it returns False as a placeholder.
        """
        return False


    def authorization_header(self, request=None) -> str:
        """
        This method will later return the value of the Authorization header.
        Currently, it returns None as a placeholder.
        """
        return None


    def current_user(self, request=None) -> User:
        """
        This method will later return the current user.
        Currently, it returns None as a placeholder.
        """
        return None
