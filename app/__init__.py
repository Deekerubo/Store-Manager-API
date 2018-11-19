import os
from flask import Flask, Blueprint, render_template
from flask_restful import Api
from instance.config import app_config
from .api.v1 import version1 as cart_BP
from .api.v2 import version2 as BD_cart
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from app.api.database import create_tables, destroy_tables
from app.api.v2.models.user_models import User

def create_app(config_name):
    app =Flask(__name__, instance_relative_config=True)
    CORS(app)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    app.config["JWT_SECRET_KEY"] = "SECRET"
    app.config['PROPAGATE_EXCEPTIONS'] = True
    app.config['JWT_BLACKLIST_ENABLED'] = True
    app.config['JWT_BLACKLIST_TOKEN_CHECKS'] = ['access']
    jwt = JWTManager(app)


    @jwt.token_in_blacklist_loader
    def check_if_token_in_blacklist(decrypted_token):
        jti = decrypted_token['jti']
        user = User()
        return user.check_token(jti)
    
    create_tables()

    '''Register my blueprints'''
    app.register_blueprint(cart_BP)
    app.register_blueprint(BD_cart)
   
    @app.route("/")
    def index():
        return render_template("docs.html")
    return app