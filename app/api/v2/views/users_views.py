import re
from werkzeug.security import check_password_hash, generate_password_hash
from flask import jsonify, make_response,request
from flask_restful import Resource,reqparse
from flask_jwt_extended import (create_access_token, jwt_required, jwt_refresh_token_required, get_raw_jwt)
from app.api.v2.models.user_models import User
from app.api.v2.utils.decorators import admin_only

parser = reqparse.RequestParser()
parser.add_argument('username' , help='Username cannot be blank', type=str)
parser.add_argument('email', required=True, help='Email cannot be blank', type=str)
parser.add_argument('password', required=True, help='Password cannot be blank', type=str)
parser.add_argument('role',  type=int)

  

class UserRegistration(Resource):
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
        
        # this_user = User.find_by_username(username)
        # print(this_user)
        # if this_user != None:
        #     return {'message': 'username already exist'},400

        # '''check if authorized for signup'''
        # # print(email)
        # user = User().is_admin(email)
        # if user != True:
        #     return make_response(jsonify({'message' : 'You are not authorized to perform this function'}), 401)


        # '''send validated user input to user model'''
        new_user = User(
            username,
            email,
            generate_password_hash(raw_password),
            role
                       )
        
        try:
            result = new_user.save_user()
            access_token = create_access_token(identity = username)
            return {
                'message': 'Store attendant was created succesfully',
                'status': 'ok',
                'access_token': access_token,
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
        check_user = User.find_by_email(self,email)

        if check_user is None:
            return {'message': 'invalid credentials'},400
        c_p = check_user[3]

        '''This compares the users password and the hashed password'''
        if not check_password_hash(c_p, password):
            return{'message':'invalid credentials'}, 400
        access_token = create_access_token(identity =  email)
        return {
                'message': 'User was logged in succesfully',
                'status':'ok',
                'access_token': access_token
                },200
    
class Logout(Resource):
    '''Logout a user'''
    @jwt_required
    def post(self):
        jti = get_raw_jwt()['jti']
        logout_token= """INSERT INTO
                tokens (token) VALUES ('{}')""" .format(jti)
        cur.execute(logout_token)
        conn.commit()
        return {"status":"Success!","message": " User successfully logged out"}, 200
