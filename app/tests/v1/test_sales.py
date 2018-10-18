import unittest
import os
import json

from app import create_app

#URLs
ADD_ORDER_URL = '/api/v1/sales'
GET_SINGLE_ORDER = '/api/v1/sales/1'
GET_ALL_ORDERS = '/api/v1/sales'


class Test_Order_Case(unittest.TestCase):
    def setUp(self):
        '''Initialize app and define test variables'''
        self.app = create_app('testing')
        self.client = self.app.test_client()
        self. orders_item = { "name": "name",
                                "description":"description",
                                "quantity":"quantity",
                                "price":"price",
                                "category":"category"
                            }
    def test_add_order(self):
        '''Test for sales '''
        response = self.client.post(ADD_ORDER_URL,
                                    data = json.dumps(self.orders_item), 
                                    content_type = 'application/json')
        self.assertEqual(response.status_code, 201)

    def test_get_single_order(self):
        '''Test to get a single order'''

        '''Add a product'''
        response = self.client.post(ADD_ORDER_URL,
                                    data = json.dumps(self.orders_item), 
                                    content_type = 'application/json')
        self.assertEqual(response.status_code, 201)

        '''return a single order from the order records'''
        response = self.client.get(GET_SINGLE_ORDER,
                                    data = json.dumps(self.orders_item), 
                                    content_type = 'application/json')
        self.assertEqual(response.status_code, 200)
