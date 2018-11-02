from flask import Blueprint
from flask_restful import Api

from .views.product_views import Products, ProductDetails
# from .views.sales_views import Sales, SingleOrder
from .views.users_views import UserRegistration, UserLogin


version2 = Blueprint('api', __name__, url_prefix='/api/v2', template_folder = 'templates')
api = Api(version2)


api.add_resource(Products, '/products')
api.add_resource(ProductDetails, '/products/<int:id>')
# api.add_resource(Sales, '/sales')
# api.add_resource(SingleOrder, '/sales/<int:id>')
api.add_resource(UserRegistration, '/signup')
api.add_resource(UserLogin, '/login')
# api.add_resource(DeleteProduct, '/products')
# api.add_resource(Logout, '/logout')


