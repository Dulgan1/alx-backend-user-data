#!/usr/bin/env python3
""" Auth module for tge API """
from flask import request
from typing import TypeVar, List


class Auth:
    """ Defines Authentication class Auth """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Checks path in excluded_path
        """
        if path is None or not excluded_paths:
            return True

        for p in excluded_paths:
            if (p.endswith('/') and path.startswith([:-1])) or \
                    p in {path, path + '/'}:
                return False

        return True

    def authorization_header(self, request=None) -> str:
        """
        Chexks authorization header
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Current user?
        """
        return None
