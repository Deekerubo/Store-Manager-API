import unittest
import os
import json
from app import create_app

ADD_ENTRY_URL = '/api/v1/products'
GET_SINGLE_ENTRY = '/api/v1/products/1'
GET_ALL_ENTRY = '/api/v1/products'
USERLOGIN = '/api/v1/login'

class Test_Entry_Case(unittest.TestCase):
    def setUp(self):
        '''Initialize app and define test variables'''
        self.app = create_app('testing')
        self.client = self.app.test_client()
        self.entry_item = { "name":"name",
                             "description":"description",
                             "quantity":4675,
                             "price": 23,
                             "category":"category"
                          }
        # self.register_user = {"email" : "dianakerubo2@gmail.com", 
        #                     "password" : "1234",
        #                      }

        # self.user_login = { "email" : "dianakerubo2@gmail.com", 
        #                     "password" : "1234",
        #                   }

    # def login(self):
    #     res = self.client.post(USERSIGNUP_URL, 
    #                            data=json.dumps(self.register_user),
    #                            content_type = 'application/json')
    #     data = json.loads(res.data.decode())
    #     self.assertEqual(res.status_code, 201)
    #     res = self.client.post(USERLOGIN,
    #                                 data=json.dumps(self.user_login),
    #                                 content_type='application/json')
    #     return json.loads(res.get_data().decode("UTF-8"))['access_token']


    def test_add_entry(self):
        '''Test to add a new product'''
        response = self.client.post(ADD_ENTRY_URL,
                                    data = json.dumps(self.entry_item),
                                    # headers=dict(Authorization="Bearer "+self.login()), 
                                    content_type = 'application/json'                                   
                                    )
        data = json.loads(response.get_data().decode("UTF-8"))
        self.assertTrue(data['Cart_Items'] )
        self.assertEqual(response.status_code, 201)

    def test_get_single_entry(self):
        '''Test to get a single entry'''

        '''Add a product'''
        response = self.client.post(ADD_ENTRY_URL,
                                    data = json.dumps(self.entry_item),
                                    content_type = 'application/json')
        data = json.loads(response.get_data().decode("UTF-8"))
        self.assertEqual(response.status_code, 200)

        '''return a single entry of the product created'''
        response = self.client.get(GET_SINGLE_ENTRY,
                                    data = json.dumps(self.entry_item),
                                    content_type = 'application/json')
        data = json.loads(response.get_data().decode("UTF-8"))
        self.assertEqual(response.status_code, 200)

    def test_get_sale_records(self):
        '''Get a single Entry'''
        response = self.client.post(ADD_ENTRY_URL,
                                    data = json.dumps(self.entry_item),
                                    content_type = 'application/json')
        data = json.loads(response.get_data().decode("UTF-8"))        
        self.assertEqual(response.status_code, 200)

        '''Test  gets all the sale entries'''
        response = self.client.get(GET_ALL_ENTRY,
                                   content_type = 'application/json')
        data = json.loads(response.get_data().decode("UTF-8"))
        self.assertEqual(response.status_code, 200)
    
