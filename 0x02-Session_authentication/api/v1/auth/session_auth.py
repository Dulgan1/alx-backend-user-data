#!/usr/bin/env python3
"""Module defines Session auth class"""
from api.v1.auth.auth import Auth
from uuid import uuid4


class SessionAuth(Auth):
    """Implememts the session auth class"""
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """method creates a  session for user with id as user_id"""
        if user_id is None or not isinstance(user_id, str):
            return None
        session_id = str(uuid4())
        self.user_id_by_session_id[session_id] = user_id

        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """method gets and returns user_id by session_id"""
        if session_id is None or not isinstance(session_id, str):
            return None
        user_id = self.user_id_by_session_id[session_id]

        return user_id
