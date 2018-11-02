import json
import os
import re
from flask import Flask, request, jsonify, make_response
from flask_restful import Resource, Api
from flask_jwt_extended import jwt_required
from app.api.v2.models.sales_models import Sale

sales_object = Sale
class Sales(Resource):
    @jwt_required
    def post(self):
        '''Create a  sale  order'''
        data = request.get_json()

        sales_items = data['sales_items']
        quantity = data['quantity']
        price = data['price']
              
        if not sales_items:
            return make_response(jsonify({'message': 'Sale  can not be empty'}),400)
        if not isinstance(price, int):
            return {'message':'price must be integer'}
        elif not isinstance(quantity, int):
            return {'message':'quantity must be integer'}
        sale = Sale.find_sale_name(self,data['sales_items'])
        if sale:
            return {"message":"Sale item already exists!"},400

        # new_sale = Sale(sales_items, quantity, price)
        # new_sale.add_sale()
        # response =new_sale.serializer()
        # return {"message":"Sale Order created successfully!","sale":response}, 200
        sales_object.add_sale(sales_items,quantity,price)
        sale1 = sales_object.find_sale_name(sales_items)
        return{"message":"sale created succefully","sale":sale1}, 201
   

        
    @jwt_required 
    def get(self):
        '''Get all order items in the cart'''
        sales = sales_object.all_orders()
        return {"message":"created successfuly!","sales":sales}, 201
        


class SingleOrder(Resource):
    @jwt_required
    def get(self, id):
        ssale = Sale.single_order(self,id)
        if ssale is None:
            return{'message':'sale not found'}
        format_sale = {
                "product_id":sale[0],
                "name":ssale[1],
                "descrption":ssale[2],
                "quantity":ssale[3],
                "price":ssale[4],
                "category":ssale[5]
            }
        
        return format_sale
    @jwt_required
    # @admin_only
    def delete(self, id):
        dele = Sale.delete_order(self, id)
        return {'message':'sale succesfully deleted'}

    def put (self, id):
        modify = Sale.modify_items(self, id)
        return {'message':'Product updated succesfully'}, 200
