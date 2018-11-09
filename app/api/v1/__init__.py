from flask import Blueprint
from flask_restful import Api

from .views.product_views import Product, SingleProduct
from .views.sales_views import NewOrder, SingleOrder
from .views.users_views import UserRegistration, UserLogin

version1 = Blueprint('api-v1', __name__, url_prefix='/api/v1', template_folder = 'templates')
api = Api(version1)


api.add_resource(Product, '/products')
api.add_resource(SingleProduct, '/products/<int:productID>')
api.add_resource(NewOrder, '/sales')
api.add_resource(SingleOrder, '/sales/<int:salesID>')
api.add_resource(UserRegistration, '/signup')
api.add_resource(UserLogin, '/login')

