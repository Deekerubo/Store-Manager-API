"""app/api/v2/models.py contains models for the app"""
import psycopg2.extras
from psycopg2 import sql
from app.api.database import init_db

conn = init_db()
cur = conn.cursor()

class Product():
    '''Add new entry'''
    def __init__(self, name, description, quantity, price, category):
        self.name = name 
        self.description = description
        self.quantity = quantity
        self.price =price
        self.category = category
        
        
    def add_entry(self):
        '''Adds new entries'''                                                   
        product = """INSERT INTO
                 products (product_name, product_description, quantity, price, category)
                VALUES('%s','%s','%s','%s','%s')""" % (self.name, self.description, self.quantity, self.price, self.category)
          

        cur.execute(product)
        conn.commit()


    def serializer(self):
        return dict(
            name=self.name,
            description=self.description,
            quantity=self.quantity,
            price=self.price,
            category=self.category
        )
                
        
    def find_product_name(self, name):
        '''Get a product by item name'''
        try:
        
            cur.execute("""SELECT * FROM products WHERE product_name='{}'; """.format(name))
            rows = cur.fetchone()       
            return rows
        except:
            pass
    def all_products(self):
        '''Return available entries'''
        cur.execute("""SELECT * FROM products ;""")
        products = cur.fetchall()
        return products
        
    def single_product(self, id):
        '''Return a single product '''
        cur.execute("""SELECT * FROM products WHERE id='{}';""".format(id))
        sproduct = cur.fetchone()
        return sproduct
