"""
Module for Api exceptions
"""

class ApiException(Exception):
    """Base class for API exceptions"""

class AuthenticationException(ApiException):
    """Class for failed authentication exceptions"""

class ConnectionException(ApiException):
    """Class for JSON API connection exceptions"""
