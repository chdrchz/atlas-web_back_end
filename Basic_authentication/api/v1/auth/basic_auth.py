#!/usr/bin/env python3
""" Module that contains a class to handle basic authentication

    Functions:
        - def extract_base64_authorization_header(
            self, authorization_header: str
            ) -> str: Extracts base 64 part from header

        - def decode_base64_authorization_header(
            self, base64_authorization_header: str
            ) -> str: Decodes header into utf-8 format

        - def extract_user_credentials(
            self, decoded_base64_authorization_header: str
            ) -> Tuple[str, str]: Extracts the user email and password

        - def user_object_from_credentials(
            self, user_email: str, user_pwd: str
             -> User: Extracts the email and password for the current user
"""

import re
import base64
import binascii
from models.user import User
from typing import Tuple, TypeVar
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """ Class that handles basic authentication
    """

    def __init__(self):
        """ Initialization method jic
        """
        pass

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
            base_64 = base64.b64decode(base64_authorization_header,
                                       validate=True)

            # Decode to utf-8
            return base_64.decode('utf-8')
        except (binascii.Error, UnicodeDecodeError):
            return None

    def extract_user_credentials(
        self, decoded_base64_authorization_header: str
    ) -> Tuple[str, str]:
        """ Extracts the user email and password from the
            decoded Base64 authorization header

            Args:
                - self
                - decoded_base64_authorization_header: Decoded header to parse

            Return:
                - A tuple including user email and password
        """
        # No header is provided
        if decoded_base64_authorization_header is None:
            return None, None

        # Header must be a valid string
        if not isinstance(decoded_base64_authorization_header, str):
            return None, None

        # Regular expression to match the format "email:password"
        pattern = r'([^:]+):(.+)'
        match = re.fullmatch(pattern, decoded_base64_authorization_header)
        if match:
            return match.group(1), match.group(2)
        return None, None

    def user_object_from_credentials(
        self, user_email: str, user_pwd: str
    ) -> TypeVar('User'):
        """ Creates a user object from extract_user_credentials()

            Args:
                - self
                - user_email: User email
                - user_pwd: User password

            Return:
                - A user instance based off of email and password
        """
        # Email and password are empty
        if user_email is None or user_pwd is None:
            return None

        # Email and password must be valid strings
        if not isinstance(user_email, str) and not isinstance(user_pwd, str):
            return None

        try:
            users = User.search({"email": user_email})
            if not users:
                return None
            for user in users:
                if user.is_valid_password(user_pwd):
                    return user

        except Exception:
            return None
