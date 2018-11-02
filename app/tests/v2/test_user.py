import unittest
import json
import os
from app import create_app
from app.api.database import DB
# from flask_jwt_extended import create_access_token, 



USERSIGNUP_URL = '/api/v2/signup'
USERLOGIN_URL = '/api/v2/login'


class Test_User_Case(unittest.TestCase):
    def setUp(self):
        '''Initialize app and define test variables'''
        self.app = create_app()
        self.client = self.app.test_client()
        self.register_user = { "email": "diana@gmail.com", "password":"1kerubo", "role":True}
        self.register_user1 = { "email": "diana1@gmail.com", "password":"1kerubo", "role":True}
        self.login_user = { "email": "diana@gmail.com", "password":"1kerubo", "role":True}
        self.login_user1 = { "email": "diana1@gmail.com", "password":"1kerubo", "role":True}
        self.register_user_empty_email = { "email": "", "password":"12345678", "role":True}
        self.register_user_invalid_email = { "email": "test.gmailcom", "password":"12345678", "role":True}
        self.register_user_empty_password = { "email": "test@gmail.com", "password":"", "role":True}
        self.register_user_short_password = { "email": "test@gmail.com", "password":"wert", "role":True}
        self.login_user_empty_email= { "email": "", "password":"12345678", "role":True }
        self.login_user_empty_password= { "email": "diana@gmail.com", "password":"", "role":True }



    def test_sign_up_success(self):
        self.client.post('api/v2/signup',data=json.dumps({
            "name":"diana",
            "email":"diana@gmail.com",
            "password":"1234",
            "role":True}),content_type='application/json')

        login=self.client.post(USERLOGIN_URL,data=json.dumps({"email":"diana@gmail.com",
                                                              "password":"1234"
        }),content_type='application/json')
        result_login=json.loads(login.data)
        # token = result_login["access_token"]
        self.assertEqual(result_login, 400)
        res = self.client.post(USERLOGIN_URL,
                               headers=dict(Authorization="Bearer " + token), 
                               data=json.dumps(self.register_user),
                               content_type = 'application/json')
        print(res.data)
        data = json.loads(res.data.decode())
        # self.assertTrue(data['access_token'])
        self.assertEqual(res.status_code, 201)

    def test_sign_up_empty_email(self):
        res = self.client.post(USERSIGNUP_URL,
                               headers=dict(Authorization="Bearer " + token),
                               data=json.dumps(self.register_user_empty_email),
                               content_type='application/json')
        data = json.loads(res.data.decode())
        self.assertEqual(res.status_code, 400)

    def test_sign_up_invalid_email(self):
        res = self.client.post(USERSIGNUP_URL,
                               headers=dict(Authorization="Bearer " + token), 
                               data=json.dumps(self.register_user_invalid_email),
                               content_type='application/json')
        data = json.loads(res.data.decode())
        self.assertEqual(res.status_code, 400)

    def test_sign_up_empty_password(self):
        res = self.client.post(USERSIGNUP_URL,
                               headers=dict(Authorization="Bearer " + token), 
                               data=json.dumps(self.register_user_empty_password),
                               content_type='application/json')
        data = json.loads(res.data.decode())
        self.assertEqual(res.status_code, 400)

    def test_sign_up_short_password(self):
        res = self.client.post(USERSIGNUP_URL,
                               headers=dict(Authorization="Bearer " + token), 
                               data=json.dumps(self.register_user_short_password),
                               content_type='application/json')
        data = json.loads(res.data.decode())
        self.assertEqual(res.status_code, 400)

    def test_user_login(self):
        res = self.client.post(USERSIGNUP_URL, 
                               data=json.dumps(self.register_user1),
                               content_type = 'application/json')
        data = json.loads(res.data.decode())
        self.assertEqual(res.status_code, 400)

        res = self.client.post(USERLOGIN_URL,
                            #    headers=dict(Authorization="Bearer " + token),
                               data=json.dumps(self.login_user1),
                               content_type='application/json')
        data = json.loads(res.data.decode())
        self.assertTrue(data, 200)
        self.assertEqual(res.status_code, 200)

    
    def test_login_empty_email(self):
        res_login = self.client.post(USERLOGIN_URL,
                                     headers=dict(Authorization="Bearer " + token), 
                                     data=json.dumps(self.login_user_empty_email),
                                     content_type='application/json')
        data = json.loads(res_login.data.decode())
        self.assertEqual(res_login.status_code, 400)
