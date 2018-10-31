
from flask_restful import Resource, reqparse
from flask import Flask,request, make_response
from passlib.hash import pbkdf2_sha256 as sha256


class User():

    def __init__(self, email, password):
        self.user_id = len(users_list)+1
        self.username = username
        self.email = email
        self.password = password
        self.role = 0

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
