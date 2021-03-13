# -*- coding: utf-8 -*-
'''Add decorators that belong to the application here'''

from functools import wraps
from jwt import decode
from jwt.exceptions import DecodeError, InvalidSignatureError, ExpiredSignatureError
from flask import current_app, request, Response

def authorize(func):
    '''Decorator to verify that the user sent a valid token with the request'''

    @wraps(func)
    def check_authorization(*args, **kwargs):
        '''Validates the incoming JWT token. Extracts username and adds it to environ'''
        try:
            if request.cookies.get('auth_token') is None:
                return Response(status=401, headers={'WWW-Authenticate': 'Bearer'})
            token = decode(
                request.cookies.get('auth_token'),
                key=current_app.config['JWT_KEY'],
                verify=True
                )
            request.environ['username'] = token['sub']
            return func(*args, **kwargs)
        except (InvalidSignatureError, DecodeError):
            return Response(
                response='{ "error": "token_invalid"}',
                status=401,
                headers={'WWW-Authenticate': 'Bearer'})
        except ExpiredSignatureError:
            return Response(
                response='{ "error": "token_expired"}',
                status=401,
                headers={'WWW-Authenticate': 'Bearer'})
    return check_authorization
