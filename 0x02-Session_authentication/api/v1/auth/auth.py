#!/usr/bin/env python3
""" Class to manage API authentication """
from flask import request
from os import getenv
from typing import List, TypeVar


class Auth():
    """ Template for other authentication systems """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Returns true if path not in list of excluded paths
        """
        if path is None or excluded_paths is None:
            return (True)
        if path in excluded_paths or f"{path}/" in excluded_paths:
            return(False)
        return (True)

    def authorization_header(self, request=None) -> str:
        """
        Returns Flask request object or None if no authorization header
        """
        if request is None or request.headers.get('Authorization') is None:
            return (None)
        return (request.headers.get('Authorization'))

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Returns current user or None if no user
        """
        return (None)

    def session_cookie(self, request=None):
        """
        Returns cookie value from request
        """
        if request is None:
            return (None)
        cookie = getenv("SESSION_NAME")
        return (request.cookies.get(cookie))
