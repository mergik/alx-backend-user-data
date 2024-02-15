#!/usr/bin/env python3
"""Module that contains SessionAuth class definition."""
from api.v1.auth.auth import Auth
import uuid
from models.user import User


class SessionAuth(Auth):
    """Allows 'in-memory' Session ID storing"""
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """Creates a Session ID for a `user_id`"""
        # if user_id is None or type(user_id) != str:
        if user_id is None or not isinstance(user_id, str):
            return None
        session_id = str(uuid.uuid4())
        self.user_id_by_session_id[session_id] = user_id
        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """Method for retrieving a User ID"""
        if session_id is None or not isinstance(session_id, str):
            return None
        return self.user_id_by_session_id.get(session_id)

    def current_user(self, request=None):
        """
        Overloads current_user; returns a User based on a
        cookie value.
        """
        if request is None:
            return None

        session_id = self.session_cookie(request)
        if session_id is None:
            return None

        user_id = self.user_id_for_session_id(session_id)
        if user_id is None:
            return None

        user = User.get(user_id)
        return user

    def destroy_session(self, request=None):
        """Deletes the user session / logout"""
        # Check whether request exists
        if not request:
            return False
        # Check whether the request contains Session ID cookie
        session_id = self.session_cookie(request)
        if not session_id:
            return False
        # Check whether Session ID is linked to a User ID
        user_id = self.user_id_for_session_id(session_id)
        if not user_id:
            return False
        self.user_id_by_session_id.pop(session_id)
        return True
