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
                sales (sales_items, quantity, price)
                VALUES('%s','%s','%s')""" % (self.sales_items, self.quantity, self.price)
          
        cur.execute(sales)
        # conn.commit()

    def serializer(self):
        return dict(
        sales_items=self.sales_items,
        quantity=self.quantity,
        price=self.price
        )           
    def find_sale_name(self, sales_items):
        '''Get a product by item name''' 
        cur.execute("""SELECT * FROM sales WHERE sales_items='{}'; """.format(sales_items))
        rows = cur.fetchone()       
        return rows
        
    def all_orders(self):
        """Return available orders"""
        cur.execute("""SELECT * FROM sales ;""")
        sales = cur.fetchall()
        print(sales)
        return sales
        
        # conn.commit()

    def single_order(self, id):
        '''Return a single Order '''
        cur.execute("""SELECT * FROM sales WHERE id='{}';""".format(id))
        singlesale = cur.fetchone()
        return singlesale

        # conn.commit()

    def delete_order(self, id):
        '''Delete a product'''
        cur.execute("""SELECT * FROM  sales WHERE id='{}';""".format(id))
        dele = cur.fetchone()
        if not dele:
            return{'message':'sale ID not found'}
        cur.execute("""SELECT * FROM  sales WHERE id='{}';""".format(id))

    def modify_items(self, id):
        '''modify a produtct'''
        cur.execute("""SELECT * FROM sales WHERE id='{}';""".format(id))
        modify = cur.fetchone()
        if not modify:
            return{'message':'sales item not found'}
        cur.execute("""SELECT * FROM sales WHERE id='{}';""".format(id))
        # conn.commit()