import json
import os
from flask import Flask, request, jsonify, make_response, Blueprint
from flask_restful import Resource, Api
from flask_jwt_extended import jwt_required


from app.api.v2.models.product_models import Entry

# cart = []

class Product (Resource):
    def __init__(self):
        self.products = Entry()
        print(self.products)

    
        '''Create a new product'''
    # @jwt_required
    def post(self):
        data = request.get_json()

        name = data['product_name']
        description = data['product_description']
        quantity = data['quantity']
        price = data['price']
        category = data['category']

        if not isinstance(price, int):
            return {'message':'price must be integer',
                    'item': price }

        elif not isinstance(quantity, int):
            return {'message':'quantity must be integer'}

        # find_name = Entry.find_product_name(name)
        # if find_name != False:
        #     return{'message': 'item exists'} 
        
        

        new_entry = self.products.add_entry(name, description, quantity, price, category)
        # print(new_entry)
        if new_entry:
            # print(new_entry)
            return "successful"
        else:
            return "not succesful"
        # return make_response(jsonify({'Cart_Items': new_entry, 'message':'product created succesfully!'}), 201)    
   
        '''Get all products'''
    @jwt_required
    def get(self):
        return make_response(jsonify({'Cart_Items': self.products.all_entries()}), 200)
       
class SingleProduct(Resource):
    def __init__(self):
        self.products = Entry()

    @jwt_required
    def get(self, productID):
       
        item = self.products.single_entry(productID)
        if item:
            return make_response(jsonify({'Item': item}), 200)
        return make_response(jsonify("item not found"), 404) 