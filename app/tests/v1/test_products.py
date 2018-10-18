import unittest
import os
import json
from app import create_app

ADD_ENTRY_URL = '/api/v1/products'
GET_SINGLE_ENTRY = '/api/v1/products/1'
GET_ALL_ENTRY = '/api/v1/products'

class Test_Entry_Case(unittest.TestCase):
    def setUp(self):
        '''Initialize app and define test variables'''
        self.app = create_app('testing')
        self.client = self.app.test_client()
        self. entry_item = { "name": "name",
                                "description":"description",
                                "quantity":"quantity",
                                "price":"price",
                                "category":"category"
                            }