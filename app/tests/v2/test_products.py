import unittest
import os
import json
from app import create_app
from .base_test import UserAuth

ADD_ENTRY_URL = '/api/v2/products'
GET_SINGLE_ENTRY = '/api/v2/products/1'
GET_ALL_ENTRY = '/api/v2/products'

class Test_Entry_Case(UserAuth):
    '''Initialize app and define test variables'''
    entry_item = { "product_name":"name",
                            "product_description":"description",
                            "quantity":4675,
                            "price": 23,
                            "category":"category"
                        }
    

    def test_add_entry(self):
        '''Test to add a new product'''
        login = self.Auth()
        token = json.loads(login.data.decode()).get('token')
        res = self.app.post(ADD_ENTRY_URL,
                                headers=dict(Authorization="Bearer " + token),
                                data = json.dumps(self.entry_item),
                                content_type = 'application/json'
                                )
        data = json.loads(res.get_data().decode("UTF-8"))
        self.assertTrue(data['message':'product created!'])
        self.assertEqual(res.status_code, 201)

    def test_get_single_entry(self):
        '''Test to get a single entry'''
        login = self.Auth()
        token = json.loads(login.data.decode()).get('token')
        self.app.post(ADD_ENTRY_URL,
                                    data = json.dumps(self.entry_item),
                                    content_type = 'application/json')
        '''return a single entry of the product created'''
        res = self.app.get(GET_SINGLE_ENTRY,
                                    headers=dict(Authorization="Bearer " + token),
                                    data = json.dumps(self.entry_item),
                                    content_type = 'application/json')
        data = json.loads(res.get_data().decode("UTF-8"))
        self.assertTrue(data['Product!'])
        self.assertEqual(res.status_code, 200)

    def test_get_sale_records(self):
        '''Get a single Entry'''
        login = self.Auth()
        token = json.loads(login.data.decode()).get('token')
        self.app.post(ADD_ENTRY_URL,
                                    data = json.dumps(self.entry_item),
                                    content_type = 'application/json')
        '''Test  gets all the sale entries'''
        res = self.app.get(GET_ALL_ENTRY, 
                                   headers=dict(Authorization="Bearer " + token),
                                   data = json.dumps(self.entry_item),
                                   content_type = 'application/json')
        data = json.loads(res.get_data().decode("UTF-8")) 
        self.assertTrue(data['Products!'])
        self.assertEqual(res.status_code, 200)

