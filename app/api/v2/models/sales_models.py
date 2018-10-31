'''contains models for the app'''
import psycopg2.extras
from psycopg2 import sql
from app.api.database import init_db

class Order(object):

    """Add new entry"""
    def __init__(self):
        # self.db = init_db
        self.conn = init_db()
        cur = self.conn.cursor()

    def add_order(self, name, description, quantity, price, category):
        """Adds new orders"""
        try:
            # conn = init_db()
            # cur = conn.cursor()
            self.cur.execute("""
                INSERT INTO sales(sales_items, sales_description, quantity, price, category)
                VALUES(%s,%s,%s,%s)
                """,
                (name, description, quantity, price, category)) 
            conn.commit()
            return 'order created succesfully'
        

        except Exception as e:
            print(e)
            return ("order not created")

           
    #  def find_sale_name(item_name):
    
    #     return next((entry for entry in Order_List if entry['item_name'] ==item_name), False)

    def all_orders(self):
        """Return available orders"""
        try:
            # conn = init_db()
            # cur = conn.cursor()
            self.cur.execute("""SELECT * FROM sales  """)
            rows = cur.fetchall()

            return rows
        
        except Exception as e:
            print(e)
            return {'message': 'No products fetched'}, 500
        

    def single_order(self, id):
        '''Return a single Order '''
        try:
            # conn = init_db()
            # cur = conn.cursor()
            self.cur.execute("""SELECT * FROM products WHERE id='{}' """.format(id))
            rows = cur.fetchall()
        
            return rows

        except Exception as e:
            print(e)
            return {'message': 'No product fetched'}, 500