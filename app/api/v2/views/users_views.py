import re
from flask import jsonify, make_response,request
from flask_restful import Resource,reqparse
from flask_jwt_extended import (create_access_token, jwt_required, jwt_refresh_token_required, create_refresh_token)
from app.api.v1.models.user_models import User

parser = reqparse.RequestParser()
parser.add_argument('email', required=True, help='Email cannot be blank', type=str)
parser.add_argument('password', required=True, help='Password cannot be blank', type=str)
  

class UserRegistration(Resource):
    def post(self):
        '''Remove all white spaces'''
        args =  parser.parse_args()
        raw_password = args.get('password')
        email = args.get('email')

        '''Validation checks for input'''
        email_format = re.compile(
        r"(^[a-zA-Z0-9_.-]+@[a-zA-Z-]+\.[.a-zA-Z-]+$)")


        if not email:
            return make_response(jsonify({'message': 'email can not be empty'}),400)
        if not raw_password:
            return make_response(jsonify({'message': 'password cannot be empty'}),400)
        if len(raw_password) < 6:
            return make_response(jsonify({'message' : 'Password should be atleast 6 characters'}), 400)
        if not (re.match(email_format, email)):
            return make_response(jsonify({'message' : 'Invalid email'}), 400)

        '''check upon validation usename exists'''  
        this_user = User.find_by_username(username)
        if this_user != False:
            return {'message': 'username already exist'},400

        '''check if authorized for signup'''
        user = User.is_admin(user_id)
        if user != True:
            return make_response(jsonify({'message' : 'You are not authorized to perform this function'}), 401)


        '''send validated user input to user model'''
        new_user = User(
            username=username ,
            email=email,
            password = User.generate_hash(raw_password)
     
        )
        # '''Checks if password is hashed'''
        # password = User.generate_hash(raw_password)

        # data = parser.parse_args()
        # new_user = User(email=data['email'],
        #                 password=User.generate_hash(data['password'])
        #                 )
        # new_user.save_user()
        # access_token = create_access_token(identity=data["email"])
        # return{"message" : 'User {} was created'.format(data["email"]),
        #         "access_token": access_token},201 

         # attempt creating a new user in user model
        try:
            result = new_user.create_store_attendant()
            access_token = create_access_token(identity = username)
            refresh_token = create_refresh_token(identity = username)
            return {
                'message': 'Store attendant was created succesfully',
                'status': 'ok',
                'access_token': access_token,
                'refresh_token': refresh_token,
                'username ': username
                },201

        except Exception as e:
            print(e)
            return {'message': 'Something went wrong'}, 500    

class UserLogin(Resource):
    def post(self):
        '''Checks for white spaces'''
        args =  parser.parse_args()
        password = args.get('password').strip()
        email = args.get('email').strip()
        if not email:
            return {'message': 'email can not be empty'},400
        if not password:
            return {'message': 'password cannot be empty'},400
        
        '''On successful login'''
        c_user = User.find_by_email(email)
        if c_user == False:
            return {'message': 'email does not  exist'},400


        data = parser.parse_args()
        current_user = User.fetch_single_user(data['email'])

        if User.verify_hash(password, email)== True:
            access_token = create_access_token(identity=data["email"])
            return{'mesage': f'Logged in as {current_user["email"]}',
                   'access_token': access_token,
                   }, 200 
        return {'message':'wrong credentials'},400
