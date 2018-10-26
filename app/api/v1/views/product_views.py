import json
import os
from flask import Flask, request, jsonify, make_response, Blueprint
from flask_restful import Resource, Api
from flask_jwt_extended import jwt_required


from app.api.v1.models.product_models import Entry

cart = []

class Product (Resource):
    def __init__(self):
        self.products = Entry()

    
        '''Create a new product'''
    # @jwt_required
    def post(self):
        data = request.get_json()

        item_name = data['name']
        item_description = data['description']
        item_quantity = data['quantity']
        item_price = data['price']
        item_category = data['category']

        if not isinstance(item_price, int):
            return {'message':'price must be integer',
                    'item': item_price }

        elif not isinstance(item_quantity, int):
            return {'message':'quantity must be integer'}

        find_name = Entry.find_product_name(item_name)
        if find_name != False:
            return{'message': 'item exists'} 

        new_entry = self.products.add_entry(item_name, item_description, item_quantity, item_price, item_category)
        return make_response(jsonify({'Cart_Items': new_entry, 'message':'product created succesfully!'}), 201)    
   
        '''Get all products'''
    # @jwt_required
    def get(self):
        return make_response(jsonify({'Cart_Items': self.products.all_entries()}), 200)
       
class SingleProduct(Resource):
    def __init__(self):
        self.products = Entry()

    # @jwt_required
    def get(self, productID):
       
        item = self.products.single_entry(productID)
        if item:
            return make_response(jsonify({'Item': item}), 200)
        return make_response(jsonify("item not found"), 404) 