import os
from flask import Flask, Blueprint, render_template
from flask_restful import Api
from instance.config import app_config
from .api.v1 import version1 as cart_BP
from .api.v2 import version2 as BD_cart
# from app.api.database import create_tables
from flask_jwt_extended import JWTManager
from app.api.database import create_tables
# from app.api.v2.models.user_models import blacklist


def create_app():
    app =Flask(__name__, instance_relative_config=True)
    # app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    app.config["JWT_SECRET_KEY"] = "SECRET"
    # app.config['JWT_BLACKLIST_ENABLED'] = True
    # app.config['JWT_BLACKLIST_TOKEN_CHECKS'] = ['access']
    jwt = JWTManager(app)
    # @jwt.token_in_blacklist_loader
    # def check_if_token_in_blacklist(decrypted_token):
    #     jti = decrypted_token['jti']
    #     return jti
    # env =os.getenv('ENV')
    # if env=='testing':
    #     url=os.getenv("DATABASE_TEST")
    # elif env=='development':
    #     url=os.getenv('DATABASE_URL')
    create_tables()

    '''Register my blueprints'''
    app.register_blueprint(cart_BP)
    app.register_blueprint(BD_cart)
   
    @app.route("/")
    def index():
        return render_template("docs.html")
    return app