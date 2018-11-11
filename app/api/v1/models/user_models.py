
from flask_restful import Resource, reqparse
from flask import Flask,request, make_response
from passlib.hash import pbkdf2_sha256 as sha256

users_list = []

class User():

    def __init__(self, email, password):
        self.user_id = len(users_list)+1
        self.email = email
        self.password = password

    def save_user(self):
        """ save a new user """
        user = dict(user_id=self.user_id,
                    email=self.email,
                    password=self.password)

        users_list.append(user)
        return user

    @classmethod
    def fetch_single_user(cls, email):
       """ Method to get a user"""
       for user in users_list:
           if user['email'] == email:
               return user
       return f"User of ID {email} doesn't exist"

    @staticmethod
    def generate_hash(password):
       return sha256.hash(password)

    @staticmethod   
    def verify_hash(password,email):
         user = next((item for item in users_list if item["email"] == email), False)
         if user == False:
             return False
         return sha256.verify(password, user['password'] )
    @staticmethod
    def find_by_email(email):
        return next((item for item in users_list if item["email"] == email), False)
