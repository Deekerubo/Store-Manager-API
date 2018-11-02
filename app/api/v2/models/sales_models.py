'''contains models for the app'''
import psycopg2.extras
from psycopg2 import sql
from .basemodel import Basemodels
# from app.api.database import init_db

# conn = init_db()
# cur = conn.cursor()

class Sale(Basemodels):

    def __init__(self, sales_items, quantity,price):
        '''Create a sale Orders'''
        self.sales_items= sales_items
        self.quantity= quantity
        self.price= price

    def add_sale(self):
        """Adds new orders"""
        sales = """INSERT INTO
                sales (sales_items, quantity, price)
                VALUES('%s','%s','%s')""" % (self.sales_items, self.quantity, self.price)
          
        self.cursor.execute(sales)
        self.conn.commit()

    def serializer(self):
        return dict(
        sales_items=self.sales_items,
        quantity=self.quantity,
        price=self.price
        )           
    def find_sale_name(self, sales_items):
        '''Get a product by item name''' 
        self.cursor.execute("""SELECT * FROM sales WHERE sales_items='{}'; """.format(sales_items))
        rows = self.cursor.fetchone()       
        return rows

        self.conn.commit()

    def all_orders(self):
        """Return available orders"""
        self.cursor.execute("""SELECT * FROM sales ;""")
        sales = self.cursor.fetchall()
        print(sales)
        return sales
        
        self.conn.commit()

    def single_order(self, id):
        '''Return a single Order '''
        self.cursor.execute("""SELECT * FROM sales WHERE id='{}';""".format(id))
        singlesale = self.cursor.fetchone()
        return singlesale

        self.conn.commit()

    def delete_order(self, id):
        '''Delete a product'''
        self.cursor.execute("""SELECT * FROM  sales WHERE id='{}';""".format(id))
        dele = self.cursor.fetchone()
        if not dele:
            return{'message':'sale ID not found'}
        self.cursor.execute("""SELECT * FROM  sales WHERE id='{}';""".format(id))

        self.conn.commit()

    def modify_items(self, id):
        '''modify a produtct'''
        self.cursor.execute("""SELECT * FROM sales WHERE id='{}';""".format(id))
        modify = self.cursor.fetchone()
        if not modify:
            return{'message':'sales item not found'}
        self.cursor.execute("""SELECT * FROM sales WHERE id='{}';""".format(id))

        self.conn.commit()