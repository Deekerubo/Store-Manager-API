import unittest
import os
import json
from app import create_app
from app.api.database import DB
# from app.api.database import destroy_tables

ADD_ENTRY_URL = '/api/v2/products'
GET_SINGLE_ENTRY = '/api/v2/products/1'
GET_ALL_ENTRY = '/api/v2/products'
USERLOGIN = '/api/v2/login'

url=os.getenv('DATABASE_TEST')
db=DB(url)

class Test_Entry_Case(unittest.TestCase):
    def setUp(self):
        '''Initialize app and define test variables'''
        self.app = create_app()
        self.client = self.app.test_client()
        self.entry_item = { "product_name":"name",
                             "product_description":"description",
                             "quantity":4675,
                             "price": 23,
                             "category":"category"
                          }
        

    def test_add_entry(self):
        '''Test to add a new product'''
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
        response = self.client.post(ADD_ENTRY_URL,
                                    headers=dict(Authorization="Bearer " + token),
                                    data = json.dumps(self.entry_item),
                                    content_type = 'application/json'                                   
                                    )
        data = json.loads(response.get_data().decode("UTF-8"))
        self.assertTrue(data['message':'success!'])
        self.assertEqual(response.status_code, 201)

    def test_get_single_entry(self):
        '''Test to get a single entry'''

        '''Add a product'''
        response = self.client.post(ADD_ENTRY_URL,
                                    data = json.dumps(self.entry_item),
                                    content_type = 'application/json')
        data = json.loads(response.get_data().decode("UTF-8"))
        self.assertEqual(response.status_code, 201)

        '''return a single entry of the product created'''
        response = self.client.get(GET_SINGLE_ENTRY,
                                    headers=dict(Authorization="Bearer " + token),
                                    data = json.dumps(self.entry_item),
                                    content_type = 'application/json')
        data = json.loads(response.get_data().decode("UTF-8"))
        self.assertEqual(response.status_code, 200)

    def test_get_sale_records(self):
        '''Get a single Entry'''
        response = self.client.post(ADD_ENTRY_URL,
                                    data = json.dumps(self.entry_item),
                                    content_type = 'application/json')
        data = json.loads(response.get_data().decode("UTF-8"))        
        self.assertEqual(response.status_code, 401)

        '''Test  gets all the sale entries'''
        response = self.client.get(GET_ALL_ENTRY, 
                                   headers=dict(Authorization="Bearer " + token),
                                   content_type = 'application/json')
        data = json.loads(response.get_data().decode("UTF-8"))
        self.assertEqual(response.status_code, 200)

    def tearDown(self):
        db.destroy_tables()

