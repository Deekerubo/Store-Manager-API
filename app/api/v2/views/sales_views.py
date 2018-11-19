import json
import os
import re
from flask import Flask, request, jsonify, make_response
from flask_restful import Resource, Api
from flask_jwt_extended import jwt_required
from app.api.v2.models.sales_models import Sale
# from app.api.database import init_DB

# conn= init_DB()
# cursor = conn.cursor()

sales_object = Sale()
class Sales(Resource):
    @jwt_required
    def post(self):
        '''Create a  sale  order'''
        data = request.get_json()

        sales_items = data['sales_items']
        quantity = data['quantity']
        price = data['price']
              
        if not sales_items:
            return make_response(jsonify({'message': 'Sales Items Cannot be Empty!'}),400)
        if not quantity:
            return make_response(jsonify({'message': 'Quantity Items Cannot be Empty!'}),400)
        if not price:
            return make_response(jsonify({'message': 'Price Items Cannot be Empty!'}),400)
        if not isinstance(price, int):
            return {'message':'Price must be integer!'}
        elif not isinstance(quantity, int):
            return {'message':'Quantity must be integer!'}
        sale = Sale.find_sale_name(self,data['sales_items'])
        if sale:
            return {"message":"Sale item already exists!"},400

        sales_object.add_sale(sales_items,quantity,price)
        # for item in sales_items:
        #     cursor.execute("""SELECT * FROM products WHERE product_name='{}' """.fomart(item))
        #     item1 = cursor.fetchone()
        #     if item1:
        #         cursor.execute("UPDATE products SET quantity='{}' WHERE product_name='{}'".format(item1[2]-quantity,item))
        #         conn.commit()
            

        sale1 = sales_object.find_sale_name(sales_items)
        return{"message":"Sale created succefully!","sale":sale1}, 201
           
    @jwt_required 
    def get(self):
        '''Get all order items in the cart'''
        sales = sales_object.all_orders()
        return {"message":"Cart Items","sales":sales}, 200
        

class SingleOrder(Resource):
    @jwt_required
    def get(self, id):
        ssale =Sale.single_order(self, id)
        if ssale is None:
            return{'message':'sale not found'},400
        return ssale
        
    @jwt_required
    def delete(self, id):
        dele = Sale.delete_order(self, id)
        if dele is None:
            return{'messsage':'Order not found'}, 400
        return {'message':'Order succesfully deleted!'},200
        
    @jwt_required
    def put (self, id):
            data = request.get_json()
            sales_items = data.get('sales_items')
            quantity = data.get('quantity')
            price = data.get('price')
            

            sale= sales_object.single_order(id)
            if not sales_items:
                sales_items=sale['sales_items']
            if not quantity:
                quantity=sale['quantity']
            if not price:
                price=sale['price']

            sales_object.modify_items(id,sales_items,quantity,price)
            return {'message':'Order updated succesfully!'}, 200
