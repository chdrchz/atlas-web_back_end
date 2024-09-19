#!/usr/bin/env python3
""" Auth module
"""

import os
from flask import request
from typing import List, TypeVar

# Define a TypeVar for User


class Auth():
    """ Template class for all authentication systems.
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Method that searches the path

            Args:
                - self
                - path: The endpoint or URL path of the incoming request
                - excluded_paths: Paths that don't need authentication

            Return:
                - True: If the path does not exist in excluded paths,
                    or if path is none
                - False: If it does exist in excluded_paths
        """

        # No authentication required
        if path is None:
            return True

        # No authentication needed since there is nothing to exclude
        if not excluded_paths:
            return True

        # Normalize trailing slash
        if not path.endswith('/'):
            path += '/'

        # If the path matches the path in excluded paths
        for excluded in excluded_paths:
            if path.endswith('/') and path == excluded:
                return False
        return True

    def authorization_header(self, request=None) -> str:
        """ Locates the authorization header

            Args:
                - self
                - request: the header to retrieve

            Return:
                - The header retrieved in string format
        """
        if request is None:
            return None

        # Returns None if Authorization isn't found,
        # or the header itself if it is
        return request.headers.get('Authorization', None)

    def current_user(self, request=None) -> TypeVar('User'):
        """
        This method will later return the current user.
        Currently, it returns None as a placeholder.
        """
        return None

    def session_cookie(self, request=None):
        """ Returns a cookie value from a request

        Args:
            request (_type_): HTTP request. Defaults to None.
        """

        if request:
            # Get the session cookie name from the env variable
            session_name = os.getenv("SESSION_NAME", "_my_session_id")

            # Cookies is a dict within request
            return request.cookies.get(session_name)

        # Request is None
        return None
