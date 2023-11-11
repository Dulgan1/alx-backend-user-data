#!/usr/bin/env python3
""" Basic Auth module"""
from api.v1.auth.auth import Auth
import base64
from models.user import User
from typing import TypeVar


class BasicAuth(Auth):
    """Implements a basic auth class"""

    def extract_base64_authorization_header(self, authorization_header: str) \
            -> str:
        """Method extracts authorization header contents"""
        if authorization_header and isinstance(authorization_header, str) \
                and authorization_header.startswith('Basic '):
            return authorization_header[6:]
        else:
            return None

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """Method decodes base64 auth header"""
        if base64_authorization_header is None or \
                not isinstance(base64_authorization_header, str):
            return None
        try:
            return base64.b64decode(base64_authorization_header).\
                    decode('utf-8')
        except Exception:
            return None

    def extract_user_credentials(
            self, decoded_base64_authorization_header: str) -> (str, str):
        """Method extracts user details from base64 string"""
        if decoded_base64_authorization_header is None or \
                not isinstance(decoded_base64_authorization_header, str) or \
                ":" not in decoded_base64_authorization_header:
            return None, None
        email, password = decoded_base64_authorization_header.split(':')

        return email, password

    def user_object_from_credentials(
            self, user_email: str, user_pwd: str) -> TypeVar('User'):
        """Mwthod searchs for usee with email and password"""
        if user_email is None or not isinstance(user_email, str) or \
                user_pwd is None or not isinstance(user_pwd, str):
            return None

        try:
            users = User.search({'email': user_email})
        except Exception:
            return None
        for user in users:
            if user.is_valid_password(user_pwd):
                return user
        return None
