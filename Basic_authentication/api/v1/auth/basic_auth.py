#!/usr/bin/env python3
""" Empty AH class

    Functions:
        - def extract_base64_authorization_header(
            self, authorization_header: str) -> str: extracts base 64 part
"""

from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """ Class that handles basic authentication
    """

    def extract_base64_authorization_header(
        self, authorization_header: str
    ) -> str:
        """ Function that extracts the base 64 part of the header

            Args:
                - self
                - authorization_header: header to be parsed

            Return:
                - The base 64 part of the header
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
