#!/usr/bin/env python3
""" Module that contains a class to handle session authentication

    Functions:
        - create_session(self, user_id: str = None) -> str:
            - returns a session_id

        - user_id_for_session_id(self, session_id: str = None) -> str:
            - returns the value associated with the key session_id
"""

import uuid
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
