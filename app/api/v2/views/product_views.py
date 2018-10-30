import json
import os
import re
from flask import Flask, request, jsonify, make_response, Blueprint
from flask_restful import Resource, Api
from flask_jwt_extended import jwt_required

from app.api.v2.models.product_models import Entry


class Product (Resource):
    def __init__(self):
        self.products = Entry()
    # @jwt_required
    def post(self):
        '''Create a new product'''
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
        if new_entry:
            print(new_entry)
            return "successful"
        else:
            return "not succesful"
   
        
    # @jwt_required
    def GetProducts(self):
        '''Get all products'''
        if Entry.all_products():
                rows=  Entry.all_products()
                return jsonify({'message': 'product retrieved succesfully','status':'ok','products': rows})
        return jsonify({'message':'no products yet'})
       
class SingleProduct(Resource):
    def __init__(self):
        self.products = Entry()

    # @jwt_required
    def get(self, productID):
        rows=  Entry.single_product(productID)
        if rows:
            return jsonify({'message': 'product retrieved succesfully','status':'ok','products': rows},200)
        else:
            return jsonify({'message':'not found' }),404
       
      