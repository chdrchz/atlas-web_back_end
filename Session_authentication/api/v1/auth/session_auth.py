#!/usr/bin/env python3
"""_summary_
"""

import uuid
from api.v1.auth.auth import Auth


class SessionAuth(Auth):
    """_summary_

    Args:
        Auth (_type_): _description_
    """
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """_summary_

        Args:
            user_id (str, optional): _description_. Defaults to None.

        Returns:
            str: _description_
        """

        if isinstance(user_id, str) and user_id:
            # Create a session
            session_id = str(uuid.uuid4())
            self.user_id_by_session_id[session_id] = user_id
            return session_id
        
        # User_id is not a valid, non-empty string
        return None
