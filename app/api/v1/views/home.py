from flask import Flask, make_response, jsonify, request, redirect
from flask_restful import Resource
from flask_restful import Api
from flask import Blueprint

class Home(Resource):
    def get(self):
        return redirect("https://documenter.getpostman.com/view/4775740/RWgxvvBe", code=302)

home = Blueprint ('home',__name__)

api = Api(home)

api.add_resource(Home, '/')