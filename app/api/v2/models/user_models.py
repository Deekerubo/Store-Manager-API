import psycopg2
import os
from psycopg2 import sql
from flask_jwt_extended import get_raw_jwt
from flask_restful import Resource, reqparse, Api
from flask import Flask,request, make_response
from passlib.hash import pbkdf2_sha256 as sha256
from .basemodel import Basemodel


url=os.getenv('DATABASE_URL')


class User(Basemodel):
    def __init__(self):
        super().__init__()

    def save_user(self,username,email,password,role=True):
        """ save a new user """
        signup ="""INSERT INTO users(username, email, password,role)
                VALUES(%s,%s,%s,%s)"""

        self.cursor.execute(signup, (username, email, password, role))
        self.conn.commit()
               

    def fetch_single_user(self, email):
        '''checks if the username exists'''
        self.cursor.execute("""SELECT * FROM users WHERE email='{}' """.format(email))
        user = self.cursor.fetchone()
        self.conn.commit()
        return user
    
    
    def find_by_email(self,email):
        '''Checks if the email created exists'''
        self.cursor.execute("""SELECT * FROM users WHERE email='{}'""".format(email))
        
        rows = self.cursor.fetchone()
        self.conn.commit()
        return rows
        

    def revoke_token(self, token):
        """Logout user by blacklisting token"""

        # token = get_raw_jwt()['jti']
        tok= """INSERT INTO tokens(token)
                            VALUES(%s)"""
        self.cursor.execute(tok,(token))
        self.conn.commit()
        # add(token)

        # return dict(message="User log out success", status="ok"), 200
    
    def check_token(self, token):
        """Logout user by blacklisting token"""
        self.cursor.execute("""SELECT token 
        FROM tokens
        WHERE token = '{}'""",format(token))
        rows = self.cursor.fetchone()
        self.conn.commit()

        if not rows:
            return False

        return True