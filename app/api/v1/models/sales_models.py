'''contains models for the app'''
Order_List = []

class Order(object):
     """Add new entry"""
     # constructor
     def __init__(self):
        # all orders placeholder
        self.orders =Order_List

     def add_order(self, name, description, quantity, price, category):
        """Adds new orders"""

        if name and description  and quantity  and price and category:
           
                single_order_holder = {"item_id" : len(self.orders)+1,
                                       "item_name": name,
                                       "item_description": description,
                                       "item_quantity":quantity,
                                       "item_price": price,
                                       "item_category": category
                                    }
                self.orders.append(single_order_holder)
                
                return(single_order_holder)

     def find_sale_name(item_name):
    
        return next((entry for entry in Order_List if entry['item_name'] ==item_name), False)

     def all_orders(self):
        """Return available orders"""

        return self.orders

     def single_order(self, id):
         '''Return a single Order '''
         for product in self.orders:
            if product['item_id'] == id:
                return product
                False