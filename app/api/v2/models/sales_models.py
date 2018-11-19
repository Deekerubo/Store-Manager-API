'''contains models for the app'''
import os
import psycopg2.extras
from psycopg2 import sql
from .basemodel import Basemodel
from app.api.database import init_DB

conn= init_DB()
cursor = conn.cursor()

class Sale(Basemodel):
    def __init__(self):
        super().__init__()


    def add_sale(self, sales_items, quantity, price):
        """Adds new orders"""
        sales = """INSERT INTO
                sales (sales_items, quantity, price)
                VALUES('%s','%s','%s')""" % (sales_items, quantity, price)
          
        self.cursor.execute(sales)
        self.conn.commit()

           
    def find_sale_name(self, sales_items):
        '''Get a product by item name''' 
        cursor.execute("""SELECT * FROM sales WHERE sales_items='{}'""".format(sales_items))
        sales = cursor.fetchone()
        conn.commit()
        return sales


    def all_orders(self):
        """Return available orders"""
        self.cursor.execute("""SELECT * FROM sales """)
        sales = self.cursor.fetchall()
        self.conn.commit()
        return sales
        

    def single_order(self,id):
        '''Return a single Order '''
        cursor.execute("""SELECT * FROM sales WHERE id='{}';""".format(id))
        singlesale = cursor.fetchone()
        conn.commit()
        return singlesale


    def delete_order(self, id):
        '''Delete a product'''
        cursor.execute("""SELECT * FROM  sales WHERE id='{}';""".format(id))
        dele = cursor.fetchone()
        if not dele:
            return{'message':'sale ID not found'}
        cursor.execute("""DELETE FROM  sales WHERE id='{}';""".format(id))
        conn.commit()
        return{'message':'sale deleted'}, 200

    def modify_items(self, id, sales_items, quantity, price):
        '''modify a sale'''
        self.cursor.execute("""UPDATE sales
                            SET sales_items='{}',
                            quantity={},
                            price={} 
                            WHERE id='{}' RETURNING id;""".format(sales_items, quantity, price, id))
        modify = self.cursor.fetchone()
        self.conn.commit()
        if not modify:
            return{'message':'sales item not found'}
        return modify

