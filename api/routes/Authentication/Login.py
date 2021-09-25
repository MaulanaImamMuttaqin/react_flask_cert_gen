from werkzeug.security import check_password_hash, safe_str_cmp
from api.Models.models import User
from flask_restful import Resource, reqparse
from flask_jwt_extended import (create_access_token, create_refresh_token, jwt_required, get_jwt_identity)

class Login(Resource):
    def get(self):
        return {"name": "Maulana imam Muttaqin"}
    
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("email", type=str)
        parser.add_argument("password", type=str)

        args = parser.parse_args()
        current_user = User.find_by_email(args["email"])

        if not current_user:
            return {"message" : "Email or Password is Incorrect"}
        
        if check_password_hash(current_user.password, args["password"]):
            access_token = create_access_token(identity= args["email"])
            refresh_token = create_refresh_token(identity= args["email"])
            return {
                'message' : 'Login Succesfull',
                'access_token': access_token,
                'refresh_token' : refresh_token,
                'status' : True
            }
        else: 
            return {
                "message" : "wrong Credential", 
                "status" : False
            }
        # user = User.query.filter_by(email=args["email"]).first()
        # print(args)
        # if user:
        #     if check_password_hash(user.password, args["password"]):
        #         return {"status": True} 
        #     else:
        #         return {"status": False}
        # return {"status": False}   