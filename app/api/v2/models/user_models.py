import psycopg2
from psycopg2 import sql
from flask_restful import Resource, reqparse, Api
from flask import Flask,request, make_response
from passlib.hash import pbkdf2_sha256 as sha256
from app.api.database import init_db


class User():
    def __init__(self):
        self.db = init_db()
        # self.user_id = len(users_list)+1
        # self.username = username
        # self.email = email
        # self.password = password
        # self.role = 0

    def save_user(self, username, email, password, role):
        """ save a new user """
        try:
            conn = init_db()
            cur = conn.cursor()
            cur.execute(
                """
                INSERT INTO users(username, email, password,role)
                VALUES(%s,%s,%s,%s)""",
                (self.username, self.email,self.password,self.role))
            conn.commit()            
                       
            return 'attendant registered succesful'
        
        except Exception as e:
            print(e)
            return ("ran into trouble registering you")

    @staticmethod
    def find_by_id(user_id):

        cur.execute("""SELECT * FROM users WHERE id='{}' """.format(user_id))
        rows = cur.fetchone()
        if rows :
            return True
               
        return False

    @staticmethod
    def generate_hash(password):
       return sha256.hash(password)

    @staticmethod
    '''compare hashed password with the password'''
    def verify_hash(password, hash):
        return sha256.verify(password, hash)

    @staticmethod
    '''chexks if a username exists'''
    def find_by_username(username):

        cur.execute("""SELECT * FROM users WHERE username='{}' """.format(username))
        rows = cur.fetchone()
               
        return rows

    @staticmethod
    def verify_hash(password,email):
         user = next((item for item in users_list if item["email"] == email), False)
         if user == False:
             return False
         return sha256.verify(password, user['password'] )

    @staticmethod
    '''Checks if user is an admin'''
    def is_admin(user_id):

        cur.execute("""SELECT * FROM users WHERE id='{}' """.format(user_id))
        rows = cur.fetchone()
        if rows :
            if rows['role'] == 1:
                return True
            return False
               
        return False
    @staticmethod
    '''make a store attendant an admin'''
    def make_admin(attendant_id):
        role = 1
        try:
            cur.execute("""UPDATE users  SET role='{}'  WHERE id='{}' """.format(role,attendant_id))
            # db.cursor.commit()
            conn.commit()
        
            return 'store attendant has been made admin'
        except Exception as e:
            print(e)
            return {'message': 'Something went wrong'}, 500
