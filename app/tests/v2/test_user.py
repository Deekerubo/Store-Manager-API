import unittest
import json
import os
from .base_test import UserAuth
from app.api.database import create_tables, destroy_tables

USERSIGNUP_URL = '/api/v2/signup'
USERLOGIN_URL = '/api/v2/login'


class Test_User_Case(UserAuth):
    '''Initialize app and define test variables'''
    def setUp(self):
        super().setUp()
        destroy_tables()
        create_tables()
        self.signup_data = { "email": "kerubo2@gmail.com", "username":"Diana", "password":"1kerubo", "role":True}
        self.register_user1 = { "email": "diana1@gmail.com", "password":"1kerubo", "role":True}
        self.register_user_empty_email = { "email": "", "username":"Diana", "password":"1kerubo", "role":True}
        self.register_user_invalid_email = { "email": "test.gmailcom", "username":"Diana", "password":"1kerubo", "role":True}
        self.register_user_empty_password = { "email": "test@gmail.com", "username":"Diana", "password":"", "role":True}
        self.register_user_short_password = { "email": "test@gmail.com","username":"Diana", "password":"erubo", "role":True}
        self.login_data = { "email": "kerubo2@gmail.com", "password":"1kerubo"}
        self.login_user_empty_email= { "email": "", "password":"12345678"}
        self.login_user_empty_password= { "email": "diana@gmail.com", "password":""}



    def test_sign_up_success(self):
        '''Tests user signup if successful'''
        res = self.app.post(USERSIGNUP_URL,
                            data=json.dumps(self.signup_data),
                            content_type='application/json')
        data = json.loads(res.data.decode())
        self.assertEqual(data['message'], 'Store attendant was created succesfully')
        self.assertEqual(data["status"], "ok")
        self.assertEqual(res.status_code, 201)   
        #destroy_tables()   

    def test_sign_up_empty_email(self):
        '''Test signup with an emptry email address'''
        res = self.app.post(USERSIGNUP_URL,
                               data=json.dumps(self.register_user_empty_email),
                               content_type='application/json')
        data = json.loads(res.data.decode())
        self.assertEqual(data['message'], 'email cannot be empty')
        self.assertEqual(res.status_code, 400)
        # destroy_tables()

    def test_sign_up_invalid_email(self):
        '''Test signup with an invalid email address'''
        res = self.app.post(USERSIGNUP_URL,
                               data=json.dumps(self.register_user_invalid_email),
                               content_type='application/json')
        data = json.loads(res.data.decode())
        self.assertEqual(data['message'], 'Invalid email')
        self.assertEqual(res.status_code, 400)

    def test_sign_up_empty_password(self):
        '''Test signup with an empty password'''
        res = self.app.post(USERSIGNUP_URL,
                               data=json.dumps(self.register_user_empty_password),
                               content_type='application/json')
        data = json.loads(res.data.decode())
        self.assertEqual(data['message'], 'password cannot be empty')
        self.assertEqual(res.status_code, 400)

    def test_sign_up_short_password(self):
        '''Test signup with a short password'''
        res = self.app.post(USERSIGNUP_URL,
                               data=json.dumps(self.register_user_short_password),
                               content_type='application/json')
        data = json.loads(res.data.decode())
        self.assertEqual(data['message'], 'Password should be atleast 6 characters')
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
        self.assertEqual(res.status_code, 201)

    
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
        #destroy_tables()

    def test_login_empty_password(self):
        '''Test login with an empty password'''
        self.app.post(USERSIGNUP_URL, 
                               data=json.dumps(self.signup_data),
                               content_type = 'application/json')
        res = self.app.post(USERLOGIN_URL,
                                     data=json.dumps(self.login_user_empty_password),
                                     content_type='application/json')
        data = json.loads(res.data.decode())
       
        self.assertTrue(data['message'],'password cannot be empty')
        self.assertEqual(res.status_code, 400)

