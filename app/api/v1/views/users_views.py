from flask_restful import Resource,reqparse

from flask_jwt_extended import (create_access_token, jwt_required, jwt_refresh_token_required, create_refresh_token)


from app.api.v1.models.user_models import User

parser = reqparse.RequestParser()
parser.add_argument('email', required=True, help='Email cannot be blank', type=str)
parser.add_argument('password', required=True, help='Password cannot be blank', type=str)
  

class UserRegistration(Resource):
    # handle create user logic
    def post(self):
        data = parser.parse_args()
        new_user = User(email=data['email'],
                        password=User.generate_hash(data['password'])
                        )
        new_user.save_user()
        access_token = create_access_token(identity=data["email"])
        return{"message" : 'User {} was created'.format(data["email"]),
                "access_token": access_token},201     

class UserLogin(Resource):
    def post(self):
        data = parser.parse_args()
        current_user = User.fetch_single_user(data['email'])

        if User.verify_hash(data['password'], current_user["password"])== True:
            access_token = create_access_token(identity=data["email"])
            return{'mesage': f'Logged in as {current_user["email"]}',
                   'access_token': access_token,
                   }, 200 
        return {'message':'wrong credentials'},400
