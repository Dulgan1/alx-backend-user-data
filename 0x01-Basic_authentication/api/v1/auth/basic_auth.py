#!/usr/bin/env python3
""" Basic Auth module"""
from api.v1.auth.auth import Auth
import base64


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
