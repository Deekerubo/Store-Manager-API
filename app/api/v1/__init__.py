from flask import Blueprint
from flask_restful import Api

from .views.products_views import Product, SingleProduct
from .views.sales_views import NewOrder, SingleOrder

version1 = Blueprint('api', __name__, url_prefix='/api/v1')
api = Api(version1)


api.add_resource(Product, '/products')
api.add_resource(SingleProduct, '/products/<int:productID>')
api.add_resource(NewOrder, '/sales')
api.add_resource(SingleOrder, '/sales/<int:salesID>')