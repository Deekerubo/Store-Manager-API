import psycopg2
from psycopg2 import sql
from flask_restful import Resource, reqparse, Api
from flask import Flask,request, make_response
from passlib.hash import pbkdf2_sha256 as sha256
from app.api.database import init_db

conn = init_db()
cur = conn.cursor()
class User():
    def __init__(self, username, email, password, role):
       
        self.username = username
        self.email = email
        self.password = password
        self.role = role
    def save_user(self):
        """ save a new user """
        try:
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

    # def is_admin(self,email):
    #     '''Checks if user is an admin'''
    #     self.cur.execute("""SELECT * FROM users WHERE email='{}' """.format(email))
    #     rows = self.cur.fetchone()
    #     if rows :
    #         if rows['role'] == 1:
    #             return True
    #         return False
               
    #     return False

    # def make_admin(attendant_id):
    #     '''make a store attendant an admin'''
    #     role = 1
    #     try:
    #         cur.execute("""UPDATE users  SET role='{}'  WHERE id='{}' """.format(role,attendant_id))
    #         # db.cursor.commit()``
    #         conn.commit()
        
    #         return 'store attendant has been made admin'
    #     except Exception as e:
    #         print(e)
    #         return {'message': 'Something went wrong'}, 500

    # def find_by_id(user_id):

    #     self.cur.execute("""SELECT * FROM users WHERE id='{}' """.format(user_id))
    #     rows = self.cur.fetchone()
    #     if rows :
    #         return True
               
    #     return False


    def fetch_single_user(self, email):
        '''checks if the username exists'''
        cur.execute("""SELECT * FROM users WHERE email='{}' """.format(email))
        user = cur.fetchone()
        conn.commit() 

        return user
    
    
    def find_by_email(self,email):
        '''Checks if the email created exists'''
        cur.execute("""SELECT * FROM users WHERE email='{}' ;""".format(email))
        rows = cur.fetchone()
               
        return rows


    
    # @staticmethod
    # def make_admin(attendant_id):
    #     '''make a store attendant an admin'''
    #     role = 1
    #     try:
    #         cur.execute("""UPDATE users  SET role='{}'  WHERE id='{}' """.format(role,attendant_id))
    #         # db.cursor.commit()
    #         conn.commit()
        
    #         return 'store attendant has been made admin'
    #     except Exception as e:
    #         print(e)
    #         return {'message': 'Something went wrong'}, 500

    