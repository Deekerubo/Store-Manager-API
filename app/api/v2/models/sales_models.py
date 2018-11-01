'''contains models for the app'''
import psycopg2.extras
from psycopg2 import sql
from app.api.database import init_db

conn = init_db()
cur = conn.cursor()
class Sale():

    def __init__(self, sales_items, quantity,price):
        '''Create a sale Orderss'''
        self.sales_items= sales_items
        self.quantity= quantity
        self.price= price

    def add_sale(self):
        """Adds new orders"""
        sales = """INSERT INTO
                products (sales_items, quantity, price)
                VALUES('%s','%s','%s')""" % (self.sales_items, self.quantity, self.price)
          

        cur.execute(sales)
        conn.commit()

     def serializer(self):
            return dict(
            sales_items=self.sales_items,
            quantity=self.quantity,
            price=self.price
        )           

    def all_orders(self):
        """Return available orders"""
        cur.execute("""SELECT * FROM products ;""")
        sales = cur.fetchall()
        return sales
        

    def single_order(self, id):
        '''Return a single Order '''
        cur.execute("""SELECT * FROM products WHERE id='{}';""".format(id))
        singlesale = cur.fetchone()
        return singlesale