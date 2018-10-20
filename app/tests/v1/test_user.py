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
        self.register_user = { "email": "test@gmail.com", "password":"1kerubo"}
        self.login_user = { "email": "test@gmail.com", "password":"1kerubo" }

    def test_sign_up_success(self):
        res = self.client.post(USERSIGNUP_URL, 
                               data=json.dumps(self.register_user),
                               content_type = 'application/json')
        data = json.loads(res.data.decode())
        self.assertTrue(data['access_token'])
        self.assertEqual(res.status_code, 201)

    def test_user_login(self):
        response = self.client.post(USERLOGIN_URL,
                                    data=json.dumps(self.login_user),
                                    content_type='application/json')
        data = json.loads(response.data.decode())
        self.assertTrue(data["access_token"])
        self.assertEqual(response.status_code, 200)
