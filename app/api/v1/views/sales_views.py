import json
import os

from flask import Flask, request, jsonify, make_response
from flask_restful import Resource, Api
from flask_jwt_extended import jwt_required
from app.api.v1.models.sales_models import Order



cart = []

class NewOrder(Resource):
    def __init__(self):
        self.orders = Order()

    '''Create a  sale  order'''
    # @jwt_required
    def post(self):
        data = request.get_json()
        item_name = data['name']
        item_description = data['description']
        item_quantity = data['quantity']
        item_price = data['price']        
        item_category = data['category']
        
        if not item_description:
            return make_response(jsonify({'message': 'Sale description  can not be empty'}),400)
        if not isinstance(item_price, int):
            return {'message':'price must be integer'}

        elif not isinstance(item_quantity, int):
            return {'message':'quantity must be integer'}
        find_name = Order.find_sale_name(item_name)

        if find_name != False:
            return{'message': 'item exists'}
        new_order = self.orders.add_order(item_name,item_description, item_quantity, item_price, item_category)
        return make_response(jsonify({'Cart_Items': new_order}), 201)

        # if not item_name:
        #     return make_response(jsonify({'message': 'Sale description  can not be empty'}),400)

        # if not item_quantity:
        #     return make_response(jsonify({'message': 'Sale description  can not be empty'}),400)
        # if not item_price:
        #     return make_response(jsonify({'message': 'Sale description  can not be empty'}),400)
        # if not item_category:
        #     return make_response(jsonify({'message': 'Sale description  can not be empty'}),400)





        
    # @jwt_required 
    def get(self):
        '''Get all order items in the cart'''
        return make_response(jsonify({'Cart_Items': self.orders.all_orders()}), 200)

class SingleOrder(Resource):
    def __init__(self):
        self.orders = Order()

    # @jwt_required
    def get(self, salesID):
       
        item = self.orders.single_order(salesID)
        if item:
            return make_response(jsonify({'Item': item}), 200)
        return make_response(jsonify("item not found"), 404)
