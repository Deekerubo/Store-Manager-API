import json

#local imports
from app import create_app
from .base_test import UserAuth

#URLs
ADD_ORDER_URL = '/api/v2/sales'
GET_SINGLE_ORDER = '/api/v2/sales/1'
GET_ALL_ORDERS = '/api/v2/sales'


class Test_Order_Case(UserAuth):
    '''Initialize app and define test variables'''
    orders_item = { "sales_item": "name",
                            "quantity":35241,
                            "price":76,
                        }

    empty_sale_items = { "sales_items":"",
                                "quantity": "",
                                "price": "",
                                }

    def test_add_order(self):
        '''Test for sales '''
        login = self.Auth()
        token = json.loads(login.data.decode()).get('token')
        res = self.app.post(ADD_ORDER_URL,
                                    headers=dict(Authorization="Bearer " + token),
                                    data = json.dumps(self.orders_item),
                                    content_type = 'application/json')
        resp_data = json.loads(res.data.decode())
        self.assertTrue(resp_data['message':'Sale created successfully'])
        self.assertEqual(res.status_code, 201)


    def test_get_single_order(self):
        '''Test to get a single order'''
        login = self.Auth()
        token = json.loads(login.data.decode()).get('token')
        self.app.post(ADD_ORDER_URL,
                                    data = json.dumps(self.orders_item),
                                    content_type = 'application/json')
        res = self.app.get(GET_SINGLE_ORDER,
                                    headers=dict(Authorization="Bearer " + token),
                                    data = json.dumps(self.orders_item),
                                    content_type = 'application/json')
        resp_data = json.loads(res.data.decode())
        self.assertTrue(resp_data['Order'])
        self.assertEqual(res.status_code, 200)

    def test_get_sale_records(self):
        '''Create sale Records'''
        login = self.Auth()
        token = json.loads(login.data.decode()).get('token')
        self.app.post(ADD_ORDER_URL,
                                    data = json.dumps(self.orders_item),
                                    content_type = 'application/json')
        res = self.app.get(GET_ALL_ORDERS,
                                   headers=dict(Authorization="Bearer " + token),
                                   content_type = 'application/json')
        resp_data = json.loads(res.data.decode())
        self.assertTrue(resp_data['Cart_Items'])
        self.assertEqual(res.status_code, 200)

    def test_empty_items(self):
        '''Test for empty sale item '''
        login = self.Auth()
        token = json.loads(login.data.decode()).get('token')
        res = self.app.post(ADD_ORDER_URL,
                                    headers=dict(Authorization="Bearer " + token),
                                    data = json.dumps(self.empty_sale_items),
                                    content_type = 'application/json')
        resp_data = json.loads(res.data.decode())
        self.assertTrue(resp_data['message'], 'Sale items cannot be empty')
        self.assertEqual(res.status_code, 400)