
from flask_restful import Resource, reqparse
from flask import Flask,jsonify,request, make_response
from passlib.hash import pbkdf2_sha256 as sha256


users = []

class User():
    
    @staticmethod
    def create_user(username,email,password):
        role = 'user'
        id = len(users) + 1
        new_user = { 'id':id ,'username':username,'email':email,'password':password,'role':role}
        users.append(new_user)
        return new_user

# find if email exists
    @staticmethod
    def find_by_email(email):
        for x in users :
            listOfKeys = [key  for (key, value) in x.items() if value == email]
            if listOfKeys:
                return 1

            return 0

# find if username exists
    @staticmethod
    def find_by_username(username):
        for x in users :
            listOfKeys = [key  for (key, value) in x.items() if value == username]
            if listOfKeys:
                return 1

            return 0

# find if username exists
    @staticmethod
    def get_user_hash(email):
        for x in users :
            listOfKeys = [key  for (key, value) in x.items() if value == email]
            if listOfKeys:
                result = filter(lambda person: person['email'] == email, users)
                return result


            return 0

    # generate hash
    @staticmethod
    def generate_hash(raw_password):
        return sha256.hash(raw_password)

    # compare user password with hashed password 
    @staticmethod
    def verify_hash(password,email):
            for x in users :
                listOfKeys = [key  for (key, value) in x.items() if value == email]
                if listOfKeys:
                    result = list(filter(lambda person: person['email'] == email, users))
                    return sha256.verify(password,  result[0]['password'] )