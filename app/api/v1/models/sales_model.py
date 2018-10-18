'''contains models for the app'''
Order_List = []

class Order(object):
     """Add new entry"""
     # constructor
     def __init__(self):
        # all orders placeholder
        self.orders =Order_List

     def add_order(self, name, description, price, quantity, category):
        """Adds new orders"""

        if name and description  and price and quantity and category:
           
                single_order_holder = {"item_id" : len(self.orders)+1,
                                       "item_name": name,
                                       "item_description": description,
                                       "item_quantity":quantity,
                                       "item_price": price,
                                       "item_category": category
                                    }
                self.orders.append(single_order_holder)
                
                return(single_order_holder)

                
     def all_orders(self):
            """Return available orders"""

        return self.orders