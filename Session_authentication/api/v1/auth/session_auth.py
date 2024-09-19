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

        try:
            if user_id is not None or isinstance(user_id, str):
                # Create a session
                self.session_id = str(uuid.uuid4())
                self.user_id_by_session_id[self.session_id] = user_id
        except Exception as e:
            return None
