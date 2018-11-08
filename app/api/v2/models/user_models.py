import psycopg2
import os
from psycopg2 import sql
from flask_restful import Resource, reqparse, Api
from flask import Flask,request, make_response
from passlib.hash import pbkdf2_sha256 as sha256
from .basemodel import Basemodel


url=os.getenv('DATABASE_URL')


class User(Basemodel):
        
    def save_user(self,username,email,password,role=False):
        """ save a new user """

        signup ="""INSERT INTO users(username, email, password,role)
                VALUES(%s,%s,%s,%s)""" % (username, email,password,role)

        self.cursor.execute(signup)
        self.conn.commit()            
                       

    def fetch_single_user(self, email):
        '''checks if the username exists'''
        self.cursor.execute("""SELECT * FROM users WHERE email='{}' """.format(email))
        user = self.cursor.fetchone()

        return user
    
    
    def find_by_email(self,email):
        '''Checks if the email created exists'''
        self.cursor.execute("""SELECT * FROM users WHERE email='{}'""".format(email))
        rows = self.cursor.fetchone()
        return rows

    # def logout_user(self):
    #     """Logout user by blacklisting token"""
    #     token = get_raw_jwt()['jti']
    #     blacklist.add(token)
    #     return dict(message="User log out success", status="ok"), 200
    
    