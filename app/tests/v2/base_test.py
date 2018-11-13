#user testcase for all tests
import os
import json
import unittest

# from run import app
from app import create_app
from app.api.database import create_tables, destroy_tables
# from app.api.database import  conn
#con = init_DB()
# cur = conn.cursor()


USERLOGIN_URL = 'api/v2/login'
USERSIGNUP_URL = 'api/v2/signup'

config_name=('testing')
app = create_app(config_name)


class UserAuth(unittest.TestCase):
    """
    Base Test Case
    """
    signup_data = {

        "username":"diana",
        "email":"diana@gmail.com",
        "role":True,
        "password":"1kerubo"
                  }
    login_data = {
        "email":"diana@gmail.com",
        "password":"1kerubo"
                }            
    def setUp(self):
        # print(conn)
        # app.testing = True
        self.app = app.test_client()
        # create_tables()
    def Auth(self, data):
        self.app.post(USERSIGNUP_URL,
                      data=json.dumps(data),
                      content_type='application/json')
        return self.app.post(USERLOGIN_URL,
                             data=json.dumps(data),
                             content_type='application/json')

    # def tearDown(self):
    #     cur.execute("DROP TABLE IF EXISTS users")
    #     conn.commit()