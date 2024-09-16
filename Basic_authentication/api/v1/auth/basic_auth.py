#!/usr/bin/env python3
""" Empty AH class

    Functions:
        - def extract_base64_authorization_header(self, authorization_header: str) -> str:
"""

from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """ This will do something in the future
    """

    def extract_base64_authorization_header(self, authorization_header: str) -> str:
        """ Function that 
        """
        # No header is provided
        if authorization_header is None:
            return None

        # Header must be a valid string
        if not isinstance(authorization_header, str):
            return None

        header = "Basic "

        # Header must start with Basic
        if authorization_header.startswith(header):

            # Calculate the position at the end of header
            start_index = len(header)
            return authorization_header[start_index:]
        else:
            return None
