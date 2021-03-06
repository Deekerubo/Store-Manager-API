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
                                "quantity":35241,
                                "price":76,
                                "category":"category"
                            }
        self.empty_sale_description = { "name":"flashdrive",
                                        "description": "", 
                                        "quantity":12,
                                        "price":300,
                                        "category":"elecronics" 
                                      }
        self.empty_sale_items = { "name":"",
                                  "description":"", 
                                  "quantity": "",
                                  "price": "",
                                  "category":"" 
                                 }
 
    def test_add_order(self):
        '''Test for sales '''
        response = self.client.post(ADD_ORDER_URL,
                                    data = json.dumps(self.orders_item),
                                    content_type = 'application/json')
        resp_data = json.loads(response.data.decode())
        self.assertTrue(resp_data['Cart_Items'])
        self.assertEqual(response.status_code, 201)


    def test_get_single_order(self):
        '''Test to get a single order'''

        '''Add a product'''
        response = self.client.post(ADD_ORDER_URL,
                                    data = json.dumps(self.orders_item),
                                    content_type = 'application/json')
        self.assertEqual(response.status_code, 200)

        '''return a single order from the order records'''
        response = self.client.get(GET_SINGLE_ORDER,
                                    data = json.dumps(self.orders_item),
                                    content_type = 'application/json')
        resp_data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)

    def test_get_sale_records(self):
        '''Create sale Records'''
        response = self.client.post(ADD_ORDER_URL,
                                    data = json.dumps(self.orders_item),
                                    content_type = 'application/json')
        self.assertEqual(response.status_code, 200)

        '''Test  gets all the sale records'''
        response = self.client.get(GET_ALL_ORDERS,
                                   content_type = 'application/json')
        resp_data = json.loads(response.data.decode())
        self.assertTrue(resp_data['Cart_Items'])
        self.assertEqual(response.status_code, 200)

    def test_empty_description(self):
        '''Test for empty sale description '''
        response = self.client.post(ADD_ORDER_URL,
                                    data = json.dumps(self.empty_sale_description), 
                                    content_type = 'application/json')
        resp_data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 400)

    # def test_empty_items(self):
    #     '''Test for empty sale item '''
    #     response = self.client.post(ADD_ORDER_URL,
    #                                 data = json.dumps(self.empty_sale_items),
    #                                 content_type = 'application/json')
    #     resp_data = json.loads(response.data.decode())
    #     self.assertTrue(resp_data['message'] == 'Sale items  can not be empty')
    #     self.assertEqual(response.status_code, 400)