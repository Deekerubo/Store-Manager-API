from flask import Flask, Blueprint, render_template
from flask_restful import Api
from instance.config import app_config
from .api.v1 import version1 as cart_BP
from flask_jwt_extended import JWTManager
# from .api.v1.views.home import home

def create_app(config_name ="development"):
    app =Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    app.config["JWT_SECRET_KEY"] = "SECRET"
    jwt = JWTManager(app)

    '''Register my blueprints'''
    app.register_blueprint(cart_BP)
   
    @app.route("/")
    def index():
        return render_template("docs.html")
    return app