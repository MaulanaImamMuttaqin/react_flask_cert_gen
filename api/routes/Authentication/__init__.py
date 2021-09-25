from flask_restful import Api
from flask import Blueprint
from .Login import Login
from .Registration import Registration


auth = Blueprint("auth",__name__)

api = Api(auth)

api.add_resource(Login, "/login")
api.add_resource(Registration, "/register")