import json
import os
import re
from flask import Flask, request, jsonify, make_response, Blueprint
from flask_restful import Resource, Api
from flask_jwt_extended import jwt_required

from app.api.v2.models.product_models import Product


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

        if not description:
            return make_response(jsonify({'message': 'Sale description  can not be empty'}),400)
        if not isinstance(price, int):
            return {'message':'price must be integer',
                    'item': price }
        elif not isinstance(quantity, int):
            return {'message':'quantity must be integer'}

        new_entry = Product(name, description, quantity, price, category)
        new_entry.add_entry()
        res =new_entry.serializer()
        return {"message":"sucess!","product":res}
        
    @jwt_required
    def get(self):
        '''Get all products'''
        products = Product.all_products(self)
        all_ps = []
        for p in products:
            format_p = {
                "product_id":p[0],
                "name":p[1],
                "descrption":p[2],
                "quantity":p[3],
                "price":p[4],
                "category":p[5]
            }
            all_ps.append(format_p)
        return {"message":"Suceess!","products":all_ps}


class ProductDetails(Resource):
    @jwt_required
    def get(self,id):
        prod = Product.single_product(self,id)
        if prod is None:
            return{'message':'product not found'}
        format_p = {
                "product_id":prod[0],
                "name":prod[1],
                "descrption":prod[2],
                "quantity":prod[3],
                "price":prod[4],
                "category":prod[5]
            }
        
        return format_p
       
      