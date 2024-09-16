#!/usr/bin/env python3
""" Module that contains a class to handle basic authentication

    Functions:
        - def extract_base64_authorization_header(
            self, authorization_header: str
            ) -> str: Extracts base 64 part
"""

import base64
import binascii
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
                - authorization_header: Header to be parsed

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

    def decode_base64_authorization_header(
        self, base64_authorization_header: str
        ) -> str:
        """ Function that handles decoding the base64 header

            Args:
                - self
                - base64_authorization_header: Header to be decoded

            Return:
                - The decoded value of the header
        """
         # No header is provided
        if base64_authorization_header is None:
            return None

        # Header must be a valid string
        if not isinstance(base64_authorization_header, str):
            return None
        
        # Is it valid Base64?
        try:
            base_64 = base64.b64decode(base64_authorization_header, validate=True)
            
            # Decode to utf-8
            return base_64.decode('utf-8')
        except (binascii.Error, UnicodeDecodeError):
            return None
