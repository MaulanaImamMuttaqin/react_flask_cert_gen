from os import error
from flask_restful import Resource, reqparse
from werkzeug.security import generate_password_hash
from api.Models import User
from api import db
class Registration(Resource):
    def get(self):
        return {"name": "Maulana imam Muttaqin"}
    
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("email", type=str)
        parser.add_argument("username", type=str)
        parser.add_argument("password", type=str)



        args = parser.parse_args()

        if User.find_by_email(args['email']):
            return {"message" : f"Email {args['email']} already exists"}

        new_user = User(
            username=args["username"], 
            email=args["email"], 
            password=generate_password_hash(args["password"], method="sha256") 
        )
        print(args)
        try:
            new_user.save_to_db()
            return {"message": "Success"}   

        except(error):
            print(error)
            return {"message": "Something went wrong"}, 500
