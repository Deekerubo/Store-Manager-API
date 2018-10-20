
from flask_restful import Resource, reqparse
from flask import Flask,jsonify,request, make_response
from passlib.hash import pbkdf2_sha256 as sha256


class User():

    users_list = []

    def __init__(self, username, email, password):
        self.user_id = len(self.users_list)+1
        self.username = username
        self.email = email
        self.password = password

    def save_user(self):
        """ save a new user """
        user = dict(user_id=self.user_id,
                    username=self.username,
                    email=self.email,
                    password=self.password)

        User.users_list.append(user)
        return user

    @classmethod
    def fetch_single_user(cls, email):
       """ Method to get a user"""
       for user in User.users_list:
           if user['email'] == email:
               return user
       return f"User of ID {email} doesn't exist"

    @staticmethod
    def generate_hash(password):
       return sha256.hash(password)

    @staticmethod
    def verify_hash(password, pass_hash):
       return sha256.verify(password, pass_hash)
 