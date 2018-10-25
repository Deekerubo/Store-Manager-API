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
        self.register_user_empty_email = { "email": "", "password":"12345678", "username":"test" }
        self.register_user_invalid_email = { "email": "test.gmailcom", "password":"12345678", "username":"test" }
        self.register_user_empty_password = { "email": "test@gmail.com", "password":"", "username":"test" }
        self.register_user_short_password = { "email": "test@gmail.com", "password":"wert", "username":"test" }
        # self.login_user_empty_email= { "email": "", "password":"12345678" }
        # self.login_user_empty_password= { "email": "kelvin@gmail.com", "password":"" }



    def test_sign_up_success(self):
        res = self.client.post(USERSIGNUP_URL, 
                               data=json.dumps(self.register_user),
                               content_type = 'application/json')
        data = json.loads(res.data.decode())
        self.assertTrue(data['access_token'])
        self.assertEqual(res.status_code, 201)

    def test_sign_up_empty_email(self):
        res = self.client.post(USERSIGNUP_URL, 
                               data=json.dumps(self.register_user_empty_email),
                               content_type='application/json')
        data = json.loads(res.data.decode())
        self.assertTrue(data['access_token'])
        self.assertEqual(res.status_code, 400)

    def test_sign_up_invalid_email(self):
        res = self.client.post(USERSIGNUP_URL, 
                               data=json.dumps(self.register_user_invalid_email),
                               content_type='application/json')
        data = json.loads(res.data.decode())
        self.assertTrue(data['access_token'])
        self.assertEqual(res.status_code, 400)

     def test_sign_up_empty_password(self):
            res = self.client.post(USERSIGNUP_URL, 
                                   data=json.dumps(self.register_user_empty_password),
                                   content_type='application/json')
        data = json.loads(res.data.decode())
        self.assertTrue(data['access_token'])
        self.assertEqual(res.status_code, 400)

        def test_sign_up_short_password(self):
            res = self.client.post(USERSIGNUP_URL, 
                                   data=json.dumps(self.register_user_short_password),
                                   content_type='application/json')
        data = json.loads(res.data.decode())
        self.assertTrue(data['access_token'])
        self.assertEqual(res.status_code, 400)

    def test_user_login(self):
        res = self.client.post(USERLOGIN_URL,
                                    data=json.dumps(self.login_user),
                                    content_type='application/json')
        data = json.loads(res.data.decode())
        self.assertTrue(data["access_token"])
        self.assertEqual(res.status_code, 200)

    
    def test_login_empty_email(self):
        res_login = self.client.post(LOGIN_URL, 
                                     data=json.dumps(self.login_user_empty_email),
                                     content_type='application/json')
        data = json.loads(res_login.data.decode())
        self.assertTrue(data["access_token"])
        self.assertEqual(res_login.status_code, 400)
