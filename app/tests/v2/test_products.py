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
        self.empty_product_name={"product_name":"",
                                "product_description":"description",
                                "quantity":4675,
                                "price": 23,
                                "category":"category"
                                }
        self.empty_product_description={"product_name":"name",
                                "product_description":"",
                                "quantity":4675,
                                "price": 23,
                                "category":"category"
                                }
        self.empty_product_category={"product_name":"name",
                                "product_description":"description",
                                "quantity":4675,
                                "price": 23,
                                "category":""
                                }
        self.quatinty_as_integer = { "product_name":"name",
                                "product_description":"description",
                                "quantity":"4675",
                                "price": 23,
                                "category":"category"
                                    }
        self.price_as_integer = { "product_name":"name",
                                "product_description":"description",
                                "quantity":4675,
                                "price": "23",
                                "category":"category"
                                    }
        
        
    

    def test_add_entry(self):
        '''Test to add a new product'''
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
        '''Add a product'''
        login = super(Test_Entry_Case, self).Auth(self.signup_data)
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

    def test_delete_product(self):
        login = super(Test_Entry_Case, self).Auth(self.signup_data)
        data = json.loads(login.data.decode())
        token = data['access_token']
        self.app.post(ADD_ENTRY_URL,
                                    data = json.dumps(self.entry_item),
                                    content_type = 'application/json')
        '''Test  gets all the sale entries'''
        res = self.app.delete(GET_SINGLE_ENTRY, 
                                   headers=dict(Authorization="Bearer " + token),
                                   data = json.dumps(self.entry_item),
                                   content_type = 'application/json')
        data = json.loads(res.get_data().decode("UTF-8")) 
        self.assertIn('Product Deleted!',data['message'])
        self.assertEqual(res.status_code, 200)

    def test_modify_product(self):
        login = super(Test_Entry_Case, self).Auth(self.signup_data)
        data = json.loads(login.data.decode())
        token = data['access_token']
        self.app.post(ADD_ENTRY_URL,
                                    data = json.dumps(self.entry_item),
                                    content_type = 'application/json')
        '''Test  gets all the sale entries'''
        res = self.app.put(GET_SINGLE_ENTRY, 
                                   headers=dict(Authorization="Bearer " + token),
                                   data = json.dumps(self.entry_item),
                                   content_type = 'application/json')
        data = json.loads(res.get_data().decode("UTF-8")) 
        self.assertIn('Product updated succesfully!',data['message'])
        self.assertEqual(res.status_code, 200)

    def test_empty_description(self):
        '''Test signup with an empty email address'''
        login = super(Test_Entry_Case, self).Auth(self.signup_data)
        data = json.loads(login.data.decode())
        token = data['access_token']
        res = self.app.post(ADD_ENTRY_URL,
                                headers=dict(Authorization="Bearer " + token),
                               data=json.dumps(self.empty_product_description),
                               content_type='application/json')
        data = json.loads(res.data.decode())
        self.assertEqual('Product description  can not be empty!',data['message'])
        self.assertEqual(res.status_code, 400)

    def test_empty_name(self):
        '''Test signup with an empty email address'''
        login = super(Test_Entry_Case, self).Auth(self.signup_data)
        data = json.loads(login.data.decode())
        token = data['access_token']
        res = self.app.post(ADD_ENTRY_URL,
                                headers=dict(Authorization="Bearer " + token),
                               data=json.dumps(self.empty_product_name),
                               content_type='application/json')
        data = json.loads(res.data.decode())
        self.assertEqual('Product  can not be empty!',data['message'])
        self.assertEqual(res.status_code, 400)

    def test_quantity_integer(self):
        '''Test signup with an empty email address'''
        login = super(Test_Entry_Case, self).Auth(self.signup_data)
        data = json.loads(login.data.decode())
        token = data['access_token']
        res = self.app.post(ADD_ENTRY_URL,
                                headers=dict(Authorization="Bearer " + token),
                               data=json.dumps(self.quatinty_as_integer),
                               content_type='application/json')
        data = json.loads(res.data.decode())
        self.assertEqual('Quantity must be integer!',data['message'])
        self.assertEqual(res.status_code, 400)
    
    def test_price_integer(self):
        '''Test signup with an empty email address'''
        login = super(Test_Entry_Case, self).Auth(self.signup_data)
        data = json.loads(login.data.decode())
        token = data['access_token']
        res = self.app.post(ADD_ENTRY_URL,
                                headers=dict(Authorization="Bearer " + token),
                               data=json.dumps(self.price_as_integer),
                               content_type='application/json')
        data = json.loads(res.data.decode())
        self.assertEqual('Price must be integer!',data['message'])
        self.assertEqual(res.status_code, 400)

    def product_addition_twice(self):
        '''Test signup with an empty email address'''
        login = super(Test_Entry_Case, self).Auth(self.signup_data)
        data = json.loads(login.data.decode())
        token = data['access_token']
        res = self.app.post(ADD_ENTRY_URL,
                                headers=dict(Authorization="Bearer " + token),
                               data=json.dumps(self.entry_item),
                               content_type='application/json')
        data = json.loads(res.data.decode())
        self.assertEqual('Product item already exists!',data['message'])
        self.assertEqual(res.status_code, 400)

    def test_empty_category(self):
        '''Test signup with an empty email address'''
        login = super(Test_Entry_Case, self).Auth(self.signup_data)
        data = json.loads(login.data.decode())
        token = data['access_token']
        res = self.app.post(ADD_ENTRY_URL,
                                headers=dict(Authorization="Bearer " + token),
                               data=json.dumps(self.empty_product_category),
                               content_type='application/json')
        data = json.loads(res.data.decode())
        self.assertEqual('Product category  can not be empty!',data['message'])
        self.assertEqual(res.status_code, 400)



