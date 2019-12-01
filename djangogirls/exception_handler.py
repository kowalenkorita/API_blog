import logging

from django.core.exceptions import (
    ObjectDoesNotExist,
    ValidationError,
)
from rest_framework import status
from rest_framework.exceptions import (
    APIException,
    AuthenticationFailed,
    NotAuthenticated,
    NotFound,
    ParseError,
)
from rest_framework.response import Response
from rest_framework.views import exception_handler as base_exception_handler


def handler(exc, context):
    if isinstance(exc, ObjectDoesNotExist):
        exc = NotFound()
    elif isinstance(exc, ValidationError):
        exc = ParseError(detail=exc.messages)
    if isinstance(exc, AuthenticationFailed) or isinstance(exc, NotAuthenticated):
        return Response(data=exc.get_full_details(),
                        status=status.HTTP_401_UNAUTHORIZED,
                        headers={'WWW-Authenticate': 'Session'})
    if isinstance(exc, APIException):
        return Response(data=exc.get_full_details(),
                        status=exc.status_code)
    else:
        return base_exception_handler(exc, context)
