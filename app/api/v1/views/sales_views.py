import json
import os

from flask import Flask, request, jsonify, make_response
from flask_restful import Resource, Api
from app.api.v1.models.sales_models import Order



cart = []

class NewOrder(Resource):
    def __init__(self):
        self.orders = Order()

    '''Create a  sale  order'''
    def post(self):
        data = request.get_json()
        item_name = data['name']
        item_price = data['price']
        item_description = data['description']
        item_quantity = data['quantity']
        item_category = data['category']

        new_order = self.orders.add_order(item_name, item_price, item_description, item_quantity, item_category)
        return make_response(jsonify({'Cart_Items': new_order}), 201)
