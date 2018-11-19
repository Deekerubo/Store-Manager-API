import json

#local imports
from app import create_app
from .base_test import UserAuth
from app.api.database import create_tables, destroy_tables

# Define URLs to use
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
                            "quantity": 35241,
                            "price": 76,
                                    }
        self.quantity_not_empty = { "sales_items":"sales_items",
                            "quantity": "",
                            "price": 76,
                                }
        self.price_item_not_empty = { "sales_items":"sales_items",
                            "quantity": 35241,
                            "price": "",
                                }
        self.modify_item = { "sales_items": "sales_items",
                        "quantity":35241,
                        "price":76,
                            }
        self.delete_item = { "sales_items": "sales_items",
                        "quantity":35241,
                        "price":76,
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
        self.assertIn('Sale created succefully!', resp_data['message'])
        self.assertEqual(res.status_code, 201)

    def test_get_single_order(self):
        '''Test to get a single order'''
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

    def test_empty_salesItem(self):
        '''Test sale with empty cart items'''
        login = super(Test_Order_Case, self).Auth(self.signup_data)
        data = json.loads(login.data.decode())
        token = data['access_token']
        res = self.app.post(ADD_ORDER_URL,
                                headers=dict(Authorization="Bearer " + token),
                               data=json.dumps(self.empty_sale_items),
                               content_type='application/json')
        data = json.loads(res.data.decode())
        self.assertEqual('Sales Items Cannot be Empty!',data['message'])
        self.assertEqual(res.status_code, 400)

    def test_price_empty(self):
        '''Test price is not an integer'''
        login = super(Test_Order_Case, self).Auth(self.signup_data)
        data = json.loads(login.data.decode())
        token = data['access_token']
        res = self.app.post(ADD_ORDER_URL,
                                headers=dict(Authorization="Bearer " + token),
                               data=json.dumps(self.price_item_not_empty),
                               content_type='application/json')
        data = json.loads(res.data.decode())
        self.assertEqual('Price Items Cannot be Empty!',data['message'])
        self.assertEqual(res.status_code, 400)

    def test_quantity_empty(self):
        '''Test quantity should not be empty'''
        login = super(Test_Order_Case, self).Auth(self.signup_data)
        data = json.loads(login.data.decode())
        token = data['access_token']
        res = self.app.post(ADD_ORDER_URL,
                                headers=dict(Authorization="Bearer " + token),
                               data=json.dumps(self.quantity_not_empty),
                               content_type='application/json')
        data = json.loads(res.data.decode())
        self.assertEqual('Quantity Items Cannot be Empty!',data['message'])
        self.assertEqual(res.status_code, 400)

    def test_modify_order(self):
        login = super(Test_Order_Case, self).Auth(self.signup_data)
        data = json.loads(login.data.decode())
        token = data['access_token']
        self.app.post(ADD_ORDER_URL,
                                    data = json.dumps(self.orders_item),
                                    content_type = 'application/json')
        '''Test  gets all the sale entries'''
        res = self.app.put(GET_SINGLE_ORDER, 
                                   headers=dict(Authorization="Bearer " + token),
                                   data = json.dumps(self.modify_item),
                                   content_type = 'application/json')
        data = json.loads(res.get_data().decode("UTF-8")) 
        self.assertIn('Order updated succesfully!',data['message'])
        self.assertEqual(res.status_code, 200)

    # def test_delete_order(self):
    #     '''Test  delete order'''
    #     login = super(Test_Order_Case, self).Auth(self.signup_data)
    #     data = json.loads(login.data.decode())
    #     token = data['access_token']
    #     res = self.app.delete(GET_SINGLE_ORDER, 
    #                                headers=dict(Authorization="Bearer " + token),
    #                                data = json.dumps(self.delete_item),
    #                                content_type = 'application/json')
    #     data = json.loads(res.get_data().decode("UTF-8")) 
    #     self.assertIn('Order not found',data['message'])
    #     self.assertEqual(res.status_code, 400)