import psycopg2
import os
from psycopg2 import sql
from flask_restful import Resource, reqparse, Api
from flask import Flask,request, make_response
from passlib.hash import pbkdf2_sha256 as sha256
from .basemodel import Basemodel


url=os.getenv('DATABASE_URL')


class User(Basemodel):
        
    def save_user(self,username,email,password,role=True):
        """ save a new user """
        print(username, email, password, role)
        signup ="""INSERT INTO users(username, email, password,role)
                VALUES(%s,%s,%s,%s)"""
        self.cursor.execute(signup, (username, email, password, role))
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

    def find_by_email_and_password(self, email, password):
        '''Checks if the user credential are okay'''
        self.cursor.execute("""SELECT * FROM users WHERE email AND password='{}'""".format(email))
        rows = self.cursor.fetchone()
        return rows

    # def logout_user(self):
    #     """Logout user by blacklisting token"""
    #     token = get_raw_jwt()['jti']
    #     blacklist.add(token)
    #     return dict(message="User log out success", status="ok"), 200
    
    