from flask_jwt_extended import get_jwt_identity
from functools import wraps
from app.api.v2.models.user_models import User


def admin_only(_f):
    ''' Restrict access if not admin '''
    @wraps(_f)
    def wrapper_function(*args, **kwargs):
        user = User().find_by_email(get_jwt_identity())
        

        if not user.admin:
            return {'message': 'Anauthorized access, you must be an admin to access this level'}, 401
        return _f(*args, **kwargs)
    return wrapper_function

def user_only(_f):
    ''' Restrict access if not attendant '''
    @wraps(_f)
    def wrapper_function(*args, **kwargs):
        user = User().find_by_email(get_jwt_identity())

        if user.admin:
            return {'message': 'Anauthorized access, you must be an attendant to access this level'}, 401
        return _f(*args, **kwargs)
    return wrapper_function