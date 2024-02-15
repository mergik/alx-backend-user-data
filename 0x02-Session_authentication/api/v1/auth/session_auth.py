#!/usr/bin/env python3
""" Class to manage Session authentication """
from typing import TypeVar
from api.v1.auth.auth import Auth
from flask import request
from models.user import User
from uuid import uuid4


class SessionAuth(Auth):
    """ Session Auth class """
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """
        Returns created session id for given user id
        Adds session id as key of dict with user id as value
        """
        if user_id is None or type(user_id) is not str:
            return (None)
        session_id = str(uuid4())
        self.user_id_by_session_id.update({session_id: user_id})
        return (session_id)

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """
        Return user id based on session id
        """
        if session_id is None or type(session_id) is not str:
            return (None)
        return (self.user_id_by_session_id.get(session_id))

    def current_user(self, request=None):
        """
        Return user instance based on cookie value
        """
        session_id = self.session_cookie(request)
        user_id = self.user_id_for_session_id(session_id)
        return (User.get(user_id))

    def destroy_session(self, request=None):
        """
        Deletes session id from dict
        """
        if request is None:
            return (False)
        session_id = self.session_cookie(request)
        if session_id and self.user_id_for_session_id(session_id):
            self.user_id_by_session_id.pop(session_id)
            return (True)
        return (False)
