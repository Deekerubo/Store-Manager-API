import json
import os
from flask import Flask, request, jsonify, make_response, Blueprint
from flask_restful import Resource, Api

from app.api.v1.models.product_models import Entry

cart = []

       
class SingleProduct(Resource):
    def __init__(self):
        self.products = Entry()

    def get(self, productID):
       
        item = self.products.single_entry(productID)
        if item:
            return make_response(jsonify({'Item': item}), 200)
        return make_response(jsonify("item not found"), 404) 