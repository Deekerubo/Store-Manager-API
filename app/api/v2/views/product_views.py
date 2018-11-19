import json
import os
import re
from flask import Flask, request, jsonify, make_response, Blueprint
from flask_restful import Resource, Api
from flask_jwt_extended import jwt_required

from app.api.v2.models.product_models import Product

product_object=Product()

class Products(Resource):
    @jwt_required
    def post(self):
        '''Create a new product'''
        data = request.get_json()
        name = data['product_name']
        description = data['product_description']
        quantity = data['quantity']
        price = data['price']
        category = data['category']

        if not name:
            return make_response(jsonify({'message': 'Product  can not be empty!'}),400)
        if not description:
                return make_response(jsonify({'message': 'Product description  can not be empty!'}),400)
        if not category:
                return make_response(jsonify({'message': 'Product category  can not be empty!'}),400)
        if not isinstance(price, int):
            return {'message':'Price must be integer!',
                    'item': price }, 400
        elif not isinstance(quantity, int):
            return {'message':'Quantity must be integer!'}, 400
        product = product_object.find_product_name(name)
        if product:
            return {"message":"Product item already exists!"},400

        
        product_object.add_entry(name,description,quantity,price,category)
        product1 = product_object.find_product_name(name)
        return {"message":"Product Created!","product":product1}, 201
        
    @jwt_required
    def get(self):
        '''Get all products'''
        products = product_object.all_products()
        return {"message":"All Products Retrieved","products":products}, 200


class ProductDetails(Resource):
    @jwt_required
    def get(self,id):
        prod = product_object.single_product(id)
        if prod is None:
            return{'message':'Product not Found'}   
        return prod
    
    @jwt_required
    def delete(self, id):
        dele = product_object.delete_product(id)
        if dele is None:
            return{'message':'Product not found'}
        return {'message':'Product Deleted!'}

    @jwt_required
    def put (self, id):
        
        data = request.get_json()
        name = data.get('product_name')
        description = data.get('product_description')
        quantity = data.get('quantity')
        price = data.get('price')
        category = data.get('category')

        return product_object.modify_items(id,name,description,quantity,price,category)
       
