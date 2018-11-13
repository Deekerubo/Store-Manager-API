import json

#local imports
from app import create_app
from .base_test import UserAuth
from app.api.database import create_tables, destroy_tables

#URLs
ADD_ORDER_URL = '/api/v2/sales'
GET_SINGLE_ORDER = '/api/v2/sales/1'
GET_ALL_ORDERS = '/api/v2/sales'


class Test_Order_Case(UserAuth):
    '''Initialize app and define test variables'''
    def setUp(self):
        super().setUp()
        destroy_tables()
        create_tables()
        self.orders_item = { "sales_items": "name",
                        "quantity":35241,
                        "price":76,
                            }

        self.empty_sale_items = { "sales_items":"",
                            "quantity": "",
                            "price": "",
                                    }

    def test_add_order(self):
        '''Test for sales '''
        login = super(Test_Order_Case, self).Auth(self.signup_data)
        data = json.loads(login.data.decode())
        token = data['access_token']
        res = self.app.post(ADD_ORDER_URL,
                                    headers=dict(Authorization="Bearer " + token),
                                    data = json.dumps(self.orders_item),
                                    content_type = 'application/json')
        resp_data = json.loads(res.data.decode())
        self.assertIn('sale created', resp_data['message'])
        self.assertEqual(res.status_code, 201)


    def test_get_single_order(self):
        '''Test to get a single order'''
        # login = self.Auth(self.signup_data)
        login = super(Test_Order_Case, self).Auth(self.signup_data)
        data = json.loads(login.data.decode())
        token = data['access_token']
        self.app.post(ADD_ORDER_URL,
                                    data = json.dumps(self.orders_item),
                                    content_type = 'application/json')
        res = self.app.get(GET_SINGLE_ORDER,
                                    headers=dict(Authorization="Bearer " + token),
                                    data = json.dumps(self.orders_item),
                                    content_type = 'application/json')
        resp_data = json.loads(res.data.decode())
        self.assertIn('sale not found', resp_data['message'])
        self.assertEqual(res.status_code, 200)

    def test_get_sale_records(self):
        '''Create sale Records'''
        login = super(Test_Order_Case, self).Auth(self.signup_data)
        data = json.loads(login.data.decode())
        token = data['access_token']
        self.app.post(ADD_ORDER_URL,
                                    data = json.dumps(self.orders_item),
                                    content_type = 'application/json')
        res = self.app.get(GET_ALL_ORDERS,
                                   headers=dict(Authorization="Bearer " + token),
                                   content_type = 'application/json')
        resp_data = json.loads(res.data.decode())
        self.assertIn('Cart Items', resp_data['message'])
        self.assertEqual(res.status_code, 200)

    def test_empty_items(self):
        '''Test for empty sale item '''
        # login = self.Auth(self.signup_data)
        login = super(Test_Order_Case, self).Auth(self.signup_data)
        data = json.loads(login.data.decode())
        token = data['access_token']
        res = self.app.post(ADD_ORDER_URL,
                                    headers=dict(Authorization="Bearer " + token),
                                    data = json.dumps(self.empty_sale_items),
                                    content_type = 'application/json')
        resp_data = json.loads(res.data.decode())
        self.assertIn('Sales Items Cannot be Empty', resp_data['message'])
        self.assertEqual(res.status_code, 400)