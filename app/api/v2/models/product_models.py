"""app/v2/models.py contains models for the app"""
import psycopg2.extras
from psycopg2 import sql
from app.api.database import init_db



class Entry(object):
    """Add new entry"""
    def __init__(self):
        self.db = init_db()
        
    def add_entry(self, name, description, quantity, price, category):

        """Adds new entries"""                                                   
        try:
            conn = init_db()
            cur = conn.cursor()
            cur.execute("""
                INSERT INTO products(product_name, product_description, quantity, price, category)
                VALUES(%s,%s,%s,%s,%s)
                """,
                (self.name, self.description, self.quantity, self.price, self.category, self.user_id)) 
            conn.commit()
            return 'product created succesfully'
        

        except Exception as e:
            print(e)
            return ("product not created")

            
        return single_entry_holder

    # def find_product_name(item_name):
    #     '''Get a product by item_name'''
    #     return next((entry for entry in Entries_list if entry['item_name'] ==item_name), False)

    # def all_entries(self):
    #     """Return available entries"""
    #     return self.entries
        
    # def single_entry(self, id):
    #     '''Return a single product '''
    #     for product in self.entries:
    #         if product['item_id'] == id:
    #             return product                                                                                     
    #     return False    
