import re
from werkzeug.security import check_password_hash, generate_password_hash
from flask import jsonify, make_response,request
from flask_restful import Resource,reqparse
from flask_jwt_extended import (create_access_token, jwt_required, jwt_refresh_token_required, get_raw_jwt, get_jwt_identity)
from app.api.v2.models.user_models import User

parser = reqparse.RequestParser()
parser.add_argument('username' , help='Username cannot be blank', type=str)
parser.add_argument('email', required=True, help='Email cannot be blank', type=str)
parser.add_argument('password', required=True, help='Password cannot be blank', type=str)
parser.add_argument('role',  type=bool)

  
user_object=User()
class UserRegistration(Resource):
    @jwt_required
    def post(self):
        '''Remove all white spaces'''
        
        args =  parser.parse_args()
        raw_password = args.get('password')
        email = args.get('email')
        username = args.get('username')
        role = args.get('role')

        '''Validation checks for input'''
        email_format = re.compile(
        r"(^[a-zA-Z0-9_.-]+@[a-zA-Z-]+\.[.a-zA-Z-]+$)")

        if not username:
            return make_response(jsonify({'message':'username cannot be empty'}), 400)
        if not email:
            return make_response(jsonify({'message': 'email can not be empty'}),400)
        if not raw_password:
            return make_response(jsonify({'message': 'password cannot be empty'}),400)
        if len(raw_password) < 6:
            return make_response(jsonify({'message' : 'Password should be atleast 6 characters'}), 400)
        if not (re.match(email_format, email)):
            return make_response(jsonify({'message' : 'Invalid email'}), 400)

        '''check upon validation usename exists''' 
        
        
        
        try:
            result = user_object.save_user(username,email,generate_password_hash(raw_password),role)
            # access_token = create_access_token(identity = username)
            return {
                'message': 'Store attendant was created succesfully',
                'status': 'ok',
                # 'access_token': access_token,
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
       
        check_user = user_object.find_by_email(email)
        print(check_user)
        if check_user is None:
            return {'message': 'invalid credentials'},400
        check_pass = check_user[3]

        '''This compares the users password and the hashed password'''
        if not check_password_hash(check_pass, password):
            return{'message':'invalid credentials'}, 400
        access_token = create_access_token(identity =  email)
        # access_token = create_access_token(identity ={'email': email, 'admin': admin, 'id':id})
        return {
                'message': 'User was logged in succesfully',
                'access_token': access_token
                },201
    
# class Logout(Resource):
#     '''Logout a user'''
#     @jwt_required
#     def post(self):
#        """Logout user"""
#        logout_user = User().logout_user(request.headers['Authorization'].split(" ")[1])
#        return logout_user
