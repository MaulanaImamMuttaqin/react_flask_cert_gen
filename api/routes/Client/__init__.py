from flask_restful import Api, Resource, reqparse
from flask import Blueprint

client = Blueprint("client", __name__)

api = Api(client)

class IdCertificate(Resource):
    def get(self):
        return {"message": "none"}

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("id", type=str)

        args = parser.parse_args()
        print(args["id"])
        return {"message" : f"your requested id was {args['id']}"}

class NameCertificate(Resource):
    def get(self):
        return {"message": "none"}

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("name", type=str)

        args = parser.parse_args()
        print(args["name"])
        return {"message" : f"you requested certificate with the name \"{args['name']}\""}


api.add_resource(IdCertificate, "/IdCertificate")
api.add_resource(NameCertificate, "/NameCertificate")