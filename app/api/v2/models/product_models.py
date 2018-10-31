"""app/api/v2/models.py contains models for the app"""
import psycopg2.extras
from psycopg2 import sql
from app.api.database import init_db

# conn = init_db()
# cur = conn.cursor()

class Entry(object):
    """Add new entry"""
    def __init__(self):
        conn = init_db()
        cur = conn.cursor()
        # self.db = init_db()
        
    def add_entry(self, name, description, quantity, price, category):

        """Adds new entries"""                                                   
        try:
            # conn = init_db()
            # cur = conn.cursor()
            self.cur.execute("""
                INSERT INTO products(product_name, product_description, quantity, price, category)
                VALUES(%s,%s,%s,%s,%s)
                """,
                (name, description, quantity,price, category)) 
            conn.commit()
            return 'product created succesfully'
        

        except Exception as e:
            print(e)
            return ("product not created")

            

    def find_product_name(name):
        '''Get a product by item name'''
        try:
        
            self.cur.execute("""SELECT * FROM products WHERE product_name='{}' """.format(name))
            rows = self.cur.fetchone()       
            return rows
        except:
            pass
    def all_products(self):
        """Return available entries"""
        try:
            # conn = init_db()
            # cur = conn.cursor()
            self.cur.execute("""SELECT * FROM products  """)
            rows = self.cur.fetchall()

            return rows
        
        except Exception as e:
            print(e)
            return {'message': 'No products fetched'}, 500
        
    def single_product(self, id):
        '''Return a single product '''
        try:
            # conn = init_db()
            # cur = conn.cursor()
            self.cur.execute("""SELECT * FROM products WHERE id='{}' """.format(id))
            rows = self.cur.fetchall()
        
            return rows

        except Exception as e:
            print(e)
            return {'message': 'No product fetched'}, 500
