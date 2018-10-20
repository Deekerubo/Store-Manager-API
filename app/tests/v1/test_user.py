import unittest
import json
import os

from app import create_app


USERSIGNUP_URL = '/api/v1/signup'
USERLOGIN_URL = '/api/v1/login'


class Test_User_Case(unittest.TestCase):
    def setUp(self):
        '''Initialize app and define test variables'''
        self.app = create_app('testing')
        self.client = self.app.test_client()
        self.register_user = { "email": "test@gmail.com", "password":"12345678", "username":"test" }
        self.login_user = { "email": "test@gmail.com", "password":"12345678" }

    def test_sign_up_success(self):
        res = self.client.post(USERSIGNUP_URL, data=json.dumps(self.register_user),
                                            content_type = 'application/json')
        resp_data = json.loads(res.data.decode())
        self.assertEqual(res.status_code, 201)
        self.assertEqual(resp_data['message'], 'User was created succesfully')

    def test_login_success(self):

        res_login = self.client.post(USERLOGIN_URL, data=json.dumps(self.login_user),
                                            content_type='application/json')

        resp_data = json.loads(res_login.data.decode())
        self.assertTrue(resp_data['access_token'])
        self.assertEqual(res_login.status_code, 200)
        self.assertEqual(resp_data['message'], 'User was logged in succesfully')