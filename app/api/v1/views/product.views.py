import json
import os
from flask import Flask, request, jsonify, make_response, Blueprint
from flask_restful import Resource, Api

from app.api.v1.models.product_models import Entry

cart = []

class Product (Resource):
    def __init__(self):
        self.products = Entry()

    
        '''Create a new product'''
    def post(self):
        data = request.get_json()
        item_name = data['name']
        item_price = data['price']
        item_description = data['description']
        item_quantity = data['quantity']
        item_category = data['category']

        new_entry = self.products.add_entry(item_name, item_price, item_description, item_quantity, item_category)
        return make_response(jsonify({'Cart_Items': new_entry}), 201)    
   
        '''Get all products'''
    def get(self):
        return make_response(jsonify({'Cart_Items': self.products.all_entries()}), 200)
       
class SingleProduct(Resource):
    def __init__(self):
        self.products = Entry()

    def get(self, productID):
       
        item = self.products.single_entry(productID)
        if item:
            return make_response(jsonify({'Item': item}), 200)
        return make_response(jsonify("item not found"), 404) 