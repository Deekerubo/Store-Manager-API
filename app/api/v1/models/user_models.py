import jwt

from werkzeug.security import check_password_hash, generate_password_hash

cred = []

class Base():

    '''Base class to be inherited by User and Entry classes'''   
    def update(self, data):
        # Validate keys before passing to data.
        for key in data:
            setattr(self, key, data[key])
        return self.view()

class User(Base):
    def __init__(self):
        # all entries placeholder
        self.cred = cred
    '''Class to model user'''
    def __init__(self, username, password, email):
        credential_holder = { "id": len(self.cred)+1,
                            "username":"username",
                            "password":"generate_password_hash(password)",
                            "email":"email"
                            }
        self.cred.append(credential_holder)
            
        return credential_holder

    def validate_password(self, password):
            '''Method for validating password input'''
            if check_password_hash(self.cred, password):
                return True
            return False



    