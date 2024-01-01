from flask import Flask
from flask_restx import Resource, Namespace 
from flask_restx import Api
from .extensions import api
from .resorces import ns

def create_app():
   app = Flask(__name__)
   api.init_app(app)
   api.add_namespace(ns)
   return app