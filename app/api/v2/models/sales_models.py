'''contains models for the app'''
import os
import psycopg2.extras
from psycopg2 import sql
from .basemodel import Basemodel
from app.api.database import init_DB

conn= init_DB()
cursor = conn.cursor()


# url=os.getenv('DATABASE_URL')

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
        # self.conn=psycopg2.connect(url)
        # self.cursor = self.conn.cursor()
        cursor.execute("""SELECT * FROM sales WHERE sales_items='{}'""".format(sales_items))
        sales = cursor.fetchone()
        conn.commit()
        return sales
        # self.conn=psycopg2.connect(url)
        # self.cursor = self.conn.cursor()
        # try:
        #     self.cursor.execute("""SELECT * FROM sales WHERE sales_items='{}'""".format(sales_items))
        # except Exception as e:
        #     print(e)
        # rows = self.cursor.fetchone()
        # self.conn.commit()       
        # return rows


    def all_orders(self):
        """Return available orders"""
        self.cursor.execute("""SELECT * FROM sales """)
        sales = self.cursor.fetchall()
        self.conn.commit()
        return sales
        

    def single_order(self,id):
        '''Return a single Order '''
        # self.conn=psycopg2.connect(url)
        # self.cursor = self.conn.cursor()
        cursor.execute("""SELECT * FROM sales WHERE id='{}';""".format(id))
        singlesale = cursor.fetchone()
        conn.commit()
        return singlesale


    def delete_order(self, id):
        '''Delete a product'''
        self.cursor.execute("""SELECT * FROM  sales WHERE id='{}';""".format(id))
        dele = self.cursor.fetchone()
        if not dele:
            return{'message':'sale ID not found'}
        self.cursor.execute("""SELECT * FROM  sales WHERE id='{}';""".format(id))
        self.conn.commit()
        return{'message':'sale deleted'}, 200

    def modify_items(self, id):
        '''modify a produtct'''
        self.cursor.execute("""SELECT * FROM sales WHERE id='{}';""".format(id))
        modify = self.cursor.fetchone()
        self.conn.commit()
        if not modify:
            return{'message':'sales item not found'}
        return modify

