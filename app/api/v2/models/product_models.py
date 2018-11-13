"""app/api/v2/models.py contains models for the app"""
import psycopg2.extras
import os
from psycopg2 import sql
from .basemodel import Basemodel

url=os.getenv('DATABASE_URL')

class Product(Basemodel):
    def __init__(self):
        super().__init__()
    '''Add new entry'''
        
    def add_entry(self,name, description, quantity, price, category):
        '''Adds new entries'''                                                   
        product = """INSERT INTO
                  products (product_name, product_description, quantity, price, category)
                  VALUES('%s','%s','%s','%s','%s')""" % (name, description, quantity, price, category)
        self.cursor.execute(product)
        self.conn.commit()

        return dict(message=name + ", Posted!", status_code=201)

            
    def find_product_name(self, name):
        '''Get a product by item name''' 
        self.cursor.execute("""SELECT * FROM products WHERE product_name='{}'; """.format(name))
        rows = self.cursor.fetchone()
        self.conn.commit()       
        return rows

    def all_products(self):
        '''Return available entries'''
        self.cursor.execute("""SELECT * FROM products ;""")
        products = self.cursor.fetchall()
        self.conn.commit()
        return products
        
    def single_product(self, id):
        '''Return a single product '''
        self.cursor.execute("""SELECT * FROM products WHERE id='{}';""".format(id))
        sproduct = self.cursor.fetchone()
        self.conn.commit()
        return sproduct
        

    def find_stock(self, product_id):
        self.cursor.execute("""SELECT * FROM products WHERE id='{}' """.format(product_id))
        rows = self.cursor.fetchone()
        self.conn.commit()
        return rows


    def delete_product(self, id):
        '''Delete a product'''
        self.cursor.execute("""SELECT * FROM  products WHERE id={};""".format(id))
        del1 = self.cursor.fetchone()
        self.conn.commit()
        if not del1:
            return{'message':'product ID not found'}
        self.cursor.execute("""DELETE FROM  products WHERE id={};""".format(id))
        self.conn.commit()
        return {'message':'Product Deleted'}, 200

    def modify_items(self, id,product_name,description,quantity,price,category):
        '''modify a produtct'''
        self.cursor.execute("""SELECT * FROM products WHERE id='{}';""".format(id))
        modify = self.cursor.fetchone()
        self.conn.commit()
        if not modify:
            return{'message':'product item not found'}
        return modify
