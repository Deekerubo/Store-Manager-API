import jwt

from werkzeug.security import check_password_hash, generate_password_hash

class Base():
    '''Base class to be inherited by User and Entry classes'''   
    def update(self, data):
        # Validate keys before passing to data.
        for key in data:
            setattr(self, key, data[key])
        return self.view()

class User(Base):
    '''Class to model user'''
    def __init__(self, username, password, email):
        self.username = username
        self.password = generate_password_hash(password)
        self.email = email
        self.id = None

    def validate_password(self, password):
            '''Method for validating password input'''
            if check_password_hash(self.password, password):
                return True
            return False



    