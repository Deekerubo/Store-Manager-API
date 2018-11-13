import unittest
import os
import json
from app import create_app
from .base_test import UserAuth
from app.api.database import create_tables, destroy_tables

ADD_ENTRY_URL = '/api/v2/products'
GET_SINGLE_ENTRY = '/api/v2/products/1'
GET_ALL_ENTRY = '/api/v2/products'

class Test_Entry_Case(UserAuth):
    '''Initialize app and define test variables'''
    def setUp(self):
        super().setUp()
        destroy_tables()
        create_tables()
        self.entry_item = { "product_name":"name",
                                "product_description":"description",
                                "quantity":4675,
                                "price": 23,
                                "category":"category"
                            }
    

    def test_add_entry(self):
        '''Test to add a new product'''
        # login = super().self.Auth(self.signup_data)
        login = super(Test_Entry_Case, self).Auth(self.signup_data)
        data = json.loads(login.data.decode())
        token = data['access_token']
        res = self.app.post(ADD_ENTRY_URL,
                                headers=dict(Authorization="Bearer " + token),
                                data = json.dumps(self.entry_item),
                                content_type = 'application/json'
                                )
        data = json.loads(res.get_data().decode("UTF-8"))
        self.assertIn('Product Created!', data['message'])
        self.assertEqual(res.status_code, 201)

    def test_get_single_entry(self):
        '''Test to get a single entry'''
        # login = self.Auth(self.signup_data)
        login = super(Test_Entry_Case, self).Auth(self.signup_data)
        data = json.loads(login.data.decode())
        token = data['access_token']
        self.app.post(ADD_ENTRY_URL,
                                    data = json.dumps(self.entry_item),
                                    content_type = 'application/json')
        '''return a single entry of the product created'''
        res = self.app.get(GET_SINGLE_ENTRY,
                                    headers=dict(Authorization="Bearer " + token),
                                    data = json.dumps(self.entry_item),
                                    content_type = 'application/json')
        data = json.loads(res.get_data().decode("UTF-8"))
        self.assertIn('Product not Found', data['message'])
        self.assertEqual(res.status_code, 200)

    def test_get_sale_records(self):
        '''Get a single Entry'''
        login = self.Auth(self.signup_data)
        data = json.loads(login.data.decode())
        token = data['access_token']
        self.app.post(ADD_ENTRY_URL,
                                    data = json.dumps(self.entry_item),
                                    content_type = 'application/json')
        '''Test  gets all the sale entries'''
        res = self.app.get(GET_ALL_ENTRY, 
                                   headers=dict(Authorization="Bearer " + token),
                                   data = json.dumps(self.entry_item),
                                   content_type = 'application/json')
        data = json.loads(res.get_data().decode("UTF-8")) 
        self.assertIn('All Products Retrieved',data['message'])
        self.assertEqual(res.status_code, 200)

