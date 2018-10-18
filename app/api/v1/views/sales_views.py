import json
import os

from flask import Flask, request, jsonify, make_response
from flask_restful import Resource, Api
from app.api.v1.models.sales_models import Order



cart = []
