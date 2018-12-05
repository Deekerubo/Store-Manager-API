#user testcase for all tests
import os
import json
import unittest

from app import create_app
from app.api.database import create_tables, destroy_tables


USERLOGIN_URL = 'api/v2/login'
USERSIGNUP_URL = 'api/v2/signup'

config_name=('testing')
app = create_app(config_name)


class UserAuth(unittest.TestCase):
    """Base Test Case"""
    signup_data = { "email": "kerubo2@gmail.com", "username":"Diana", "password":"1kerubo", "role":True}
    register_user1 = { "email": "diana1@gmail.com", "password":"1kerubo", "role":True}
    register_user_empty_email = { "email": "", "username":"Diana", "password":"1kerubo", "role":True}
    register_user_invalid_email = { "email": "test.gmailcom", "username":"Diana", "password":"1kerubo", "role":True}
    register_user_empty_password = { "email": "test@gmail.com", "username":"Diana", "password":"", "role":True}
    register_user_short_password = { "email": "test@gmail.com","username":"Diana", "password":"erubo", "role":True}
    login_data = { "email": "kerubo2@gmail.com", "password":"1kerubo"}
    login_user_empty_email= { "email": "", "password":"12345678"}
    login_user_empty_password= { "email": "diana@gmail.com", "password":""}
    
            
    def setUp(self):
        self.app = app.test_client()

    def Auth(self, data):
        self.app.post(USERSIGNUP_URL,
                      data=json.dumps(data),
                      contlogin_dataent_type='application/json')
        return self.app.post(USERLOGIN_URL,
                             data=json.dumps(data),
                             content_type='application/json')

