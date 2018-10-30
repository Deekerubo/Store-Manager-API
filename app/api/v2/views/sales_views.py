import json
import os

from flask import Flask, request, jsonify, make_response
from flask_restful import Resource, Api
from flask_jwt_extended import jwt_required
from app.api.v1.models.sales_models import Order


class NewOrder(Resource):
    def __init__(self):
        self.orders = Order()

    '''Create a  sale  order'''
    # @jwt_required
    def post(self):
        data = request.get_json()

        name = data['sales_items']
        description = data['sales_description']
        price = data['price']
        quantity = data['quantity']
        category = data['category']
  

        
        if not description:
            return make_response(jsonify({'message': 'Sale description  can not be empty'}),400)
        if not isinstance(price, int):
            return {'message':'price must be integer'}

        elif not isinstance(quantity, int):
            return {'message':'quantity must be integer'}
        # find_name = Order.find_sale_name(name)

        # if find_name != False:
        #     return{'message': 'item exists'}
        new_order = self.orders.add_order(name, description, quantity, price, category)
        if new_order:
            print(new_order)
            return "successful"
        else:
            return "not succesful"
   

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
        if Order.all_orders():
                rows=  Order.all_orders()
                return jsonify({'message': 'order retrieved succesfully','status':'ok','products': rows})
        return jsonify({'message':'no orders in the database yet'})

class SingleOrder(Resource):
    def __init__(self):
        self.orders = Order()

    # @jwt_required
    def get(self, salesID):
        rows=  Order.single_order(salesID)
        if rows:
            return jsonify({'message': 'order retrieved succesfully','status':'ok','products': rows},200)
        else:
            return jsonify({'message':'order ID not found' }),404
