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
    
