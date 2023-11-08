#!/usr/bin/env python3
""" Basic Auth module"""
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """Implements a basic auth class"""

    def extract_base64_authorization_header(self, authorization_header: str) \
            -> str:
        """Method extracts authorization header contents"""
        if authorization_header and authorization_header.startswith('Basic ') \
                and isinstance(authorization_header, str):
            return authorization_header[6:]
        else:
            return None
