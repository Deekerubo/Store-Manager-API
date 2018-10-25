"""app/v1/models.py contains models for the app"""
Entries_list = []

class Entry(object):
    """Add new entry"""
    # constructor
    def __init__(self):
        # all entries placeholder
        self.entries = Entries_list

    def add_entry(self, name, description, quantity, price, category):
        """Adds new entries"""

        single_entry_holder = { "item_id" : len(self.entries)+1,
                                    "item_name": name,
                                    "item_description": description,
                                    "item_quantity":quantity,
                                    "item_price": price,  
                                    "item_category": category
                               }
        self.entries.append(single_entry_holder)
            
        return single_entry_holder

    def find_product_name(item_name):

        return next((entry for entry in Entries_list if entry['item_name'] ==item_name), False)
        # return next((entry for entry in Entries_list if ['name'] == name), False)

    def all_entries(self):
        """Return available entries"""
        return self.entries
        
    def single_entry(self, id):
        '''Return a single product '''
        for product in self.entries:
            if product['item_id'] == id:
                return product
        return False    