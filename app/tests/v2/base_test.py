#user testcase for all tests
import os
import json
import unittest

#local imports
from app import create_app
from app.api.database import create_tables, destroy_tables


USERLOGIN_URL = 'api/v2/login'
USERSIGNUP_URL = 'api/v2/signup'

#config_name = 'testing'
app = create_app(os.getenv('ENV'))

class UserAuth(unittest.TestCase):
    """
    Base Test Case
    """
                 
    def setUp(self):
        signup_data = {

        "name":"diana",
        "email":"diana@gmail.com",
        "role":True,
        "password":"1kerubo"
                  }
        login_data = {
            "email":"diana@gmail.com",
            "password":"1kerubo"
                    }
        app.testing = True
        self.app = app.test_client()
        create_tables()
        
    def Auth(self):

        signup_data = {

            "name":"diana",
            "email":"diana@gmail.com",
            "role":True,
            "password":"1kerubo"
                  }
        login_data = {
            "email":"diana@gmail.com",
            "password":"1kerubo"
                    }
        self.app.post(USERSIGNUP_URL,
                      data=json.dumps(self.signup_data),
                      content_type='application/json')
        return self.app.post(USERLOGIN_URL,
                             data=json.dumps(self.login_data),
                             content_type='application/json')

    def tearDown(self):
        destroy_tables()