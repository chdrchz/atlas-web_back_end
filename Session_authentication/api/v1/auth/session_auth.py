#!/usr/bin/env python3
""" Module that contains a class to handle session authentication

    Functions:
        - create_session(self, user_id: str = None) -> str:
            - returns a session_id

        - user_id_for_session_id(self, session_id: str = None) -> str:
            - returns the value associated with the key session_id

        - def current_user(self, request=None):
            - returns a user instance based on a session cookie
"""

import uuid
from models.user import User
from api.v1.auth.auth import Auth


class SessionAuth(Auth):
    """ Class that handles session authentication
    """
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """ Method that returns a session_id

        Args:
            user_id (str): the user_id of the current user. Defaults to None.

        Returns:
            str: session_id in a json formatted string
        """

        if isinstance(user_id, str) and user_id:
            # Create a session
            session_id = str(uuid.uuid4())
            self.user_id_by_session_id[session_id] = user_id
            return session_id

        # User_id is not a valid, non-empty string
        return None

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """_summary_

        Args:
            session_id (str): session_id for session. Defaults to None.

        Returns:
            str: The value of the session_id key
        """

        if isinstance(session_id, str) and session_id:
            return self.user_id_by_session_id.get(session_id)

        # Session_id is not a valid, non-empty string
        return None

    def current_user(self, request=None):
        """ Returns a user instance based on a cookie value

        Args:
            request (_type_): HTTP request. Defaults to None.
        """
        # Get the session cookie
        session_cookie = self.session_cookie(request)

        # Get the user_id value from the key, session_cookie
        user_id = self.user_id_for_session_id(session_cookie)

        # Return user instance
        return User.get(user_id)

    def destroy_session(self, request=None):
        """ Method that deletes a session based ona session ID

        Args:
            request (_type_): request data. Defaults to None.
        """
        # Validate request
        if request is None:
            return False

        # Verify request contains the session ID cookie
        session_id = self.session_cookie(request)
        if not session_id:
            return False

        # Verify user_id
        user_id = self.user_id_for_session_id(session_id)
        if user_id is None:
            return False

        # Delete the session
        del self.user_id_by_session_id[session_id]
        return True
