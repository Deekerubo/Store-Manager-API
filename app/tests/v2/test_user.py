import unittest
import json
import os
from .base_test import UserAuth



USERSIGNUP_URL = '/api/v2/signup'
USERLOGIN_URL = '/api/v2/login'


class Test_User_Case(UserAuth):
    '''Initialize app and define test variables'''
    signup_data = { "email": "diana@gmail.com", "password":"1kerubo", "role":True}
    register_user1 = { "email": "diana1@gmail.com", "password":"1kerubo", "role":True}
    register_user_empty_email = { "email": "", "password":"1kerubo", "role":True}
    register_user_invalid_email = { "email": "test.gmailcom", "password":"1kerubo", "role":True}
    register_user_empty_password = { "email": "test@gmail.com", "password":"", "role":True}
    register_user_short_password = { "email": "test@gmail.com", "password":"1kerubo", "role":True}
    login_data = { "email": "diana@gmail.com", "password":"1kerubo"}
    login_user_empty_email= { "email": "", "password":"12345678"}
    login_user_empty_password= { "email": "diana@gmail.com", "password":""}



    def test_sign_up_success(self):
        '''Tests user signup if successful'''
        res = self.app.post(USERSIGNUP_URL,
                            data=json.dumps(self.signup_data),
                            content_type='application/json')
        data = json.loads(res.data.decode())
        self.assertEqual(data['message'], 'Store successfully created')
        self.assertEqual(res.status_code, 201)        

    def test_sign_up_empty_email(self):
        '''Test signup with an emptry email address'''
        res = self.app.post(USERSIGNUP_URL,
                               data=json.dumps(self.register_user_empty_email),
                               content_type='application/json')
        data = json.loads(res.data.decode())
        self.assertEqual(data['message'], 'Email cannot be empty')
        self.assertEqual(res.status_code, 400)

    def test_sign_up_invalid_email(self):
        '''Test signup with an invalid email address'''
        res = self.app.post(USERSIGNUP_URL,
                               data=json.dumps(self.register_user_invalid_email),
                               content_type='application/json')
        data = json.loads(res.data.decode())
        self.assertEqual(data['message'], 'Invalid Email')
        self.assertEqual(res.status_code, 400)

    def test_sign_up_empty_password(self):
        '''Test signup with an empty password'''
        res = self.app.post(USERSIGNUP_URL,
                               data=json.dumps(self.register_user_empty_password),
                               content_type='application/json')
        data = json.loads(res.data.decode())
        self.assertEqual(data['message'], 'Empty password')
        self.assertEqual(res.status_code, 400)

    def test_sign_up_short_password(self):
        '''Test signup with a short password'''
        res = self.app.post(USERSIGNUP_URL,
                               data=json.dumps(self.register_user_short_password),
                               content_type='application/json')
        data = json.loads(res.data.decode())
        self.assertEqual(data['message'], 'password should be more than 6 characters')
        self.assertEqual(res.status_code, 400)

    def test_user_login(self):
        '''Test login success'''
        self.app.post(USERSIGNUP_URL, 
                               data=json.dumps(self.signup_data),
                               content_type = 'application/json')
        res = self.app.post(USERLOGIN_URL,
                               data=json.dumps(self.login_data),
                               content_type='application/json')
        data = json.loads(res.data.decode())
        self.assertTrue(data['message'],'User Login successful')
        self.assertEqual(res.status_code, 200)

    
    def test_login_empty_email(self):
        '''Test login with an empty email'''
        self.app.post(USERSIGNUP_URL, 
                               data=json.dumps(self.signup_data),
                               content_type = 'application/json')
        res = self.app.post(USERLOGIN_URL,
                                     data=json.dumps(self.login_user_empty_email),
                                     content_type='application/json')
        data = json.loads(res.data.decode())
        self.assertTrue(data['message'],'Invalid Credentials')
        self.assertEqual(res.status_code, 400)

    def test_login_empty_password(self):
        '''Test login with an empty password'''
        self.app.post(USERSIGNUP_URL, 
                               data=json.dumps(self.signup_data),
                               content_type = 'application/json')
        res = self.app.post(USERLOGIN_URL,
                                     data=json.dumps(self.login_user_empty_password),
                                     content_type='application/json')
        data = json.loads(res.data.decode())
        self.assertTrue(data['message'],'Invalid Credentials')
        self.assertEqual(res.status_code, 400)

