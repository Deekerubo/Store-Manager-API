import unittest
import os
import json

from app import create_app
from app.api.database import DB

#URLs
ADD_ORDER_URL = '/api/v2/sales'
GET_SINGLE_ORDER = '/api/v2/sales/1'
GET_ALL_ORDERS = '/api/v2/sales'


class Test_Order_Case(unittest.TestCase):
    def setUp(self):
        '''Initialize app and define test variables'''
        self.app = create_app('testing')
        self.client = self.app.test_client()
        self. orders_item = { "sales_item": "name",
                                "quantity":35241,
                                "price":76,
                            }
   
        self.empty_sale_items = { "sales_items":"",
                                  "quantity": "",
                                  "price": "",
                                 }
 
    def test_add_order(self):
        '''Test for sales '''
        self.client.post('api/v2/signup',data=json.dumps({
            "name":"charity",
            "email":"charity@gmail.com",
            "role":True,
            "password":"1234"

        }),content_type='application/json')
        login=self.client.post(USERLOGIN,data=json.dumps({"email":"charity@gmail.com",
        "password":"1234"
        }),content_type='application/json')
        result_login=json.loads(login.data)
        token=result_login['access_token']
        response = self.client.post(ADD_ORDER_URL,
                                    headers=dict(Authorization="Bearer " + token),
                                    data = json.dumps(self.orders_item),
                                    content_type = 'application/json')
        resp_data = json.loads(response.data.decode())
        self.assertTrue(resp_data['message':'Successful'])
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
                                    headers=dict(Authorization="Bearer " + token),
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
                                   headers=dict(Authorization="Bearer " + token),
                                   content_type = 'application/json')
        resp_data = json.loads(response.data.decode())
        self.assertTrue(resp_data['Cart_Items'])
        self.assertEqual(response.status_code, 200)

    def test_empty_items(self):
        '''Test for empty sale item '''
        response = self.client.post(ADD_ORDER_URL,
                                    headers=dict(Authorization="Bearer " + token),
                                    data = json.dumps(self.empty_sale_items),
                                    content_type = 'application/json')
        resp_data = json.loads(response.data.decode())
        self.assertTrue(resp_data['message'] == 'Sale items  can not be empty')
        self.assertEqual(response.status_code, 400)