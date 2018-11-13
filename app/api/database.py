# #Cretate a Database connection
import os
import psycopg2
from urllib.parse import urlparse


dev_url = "dbname='store_manager' host='localhost' port='5432' user='postgres' password='nyambumo'"
test_url = "dbname='store_manager_tests' host='localhost' port='5432' user='postgres' password='nyambumo'"
config= os.getenv('APP_SETTINGS')
def get_connection():
    if config == 'development':
        con=psycopg2.connect(dev_url)
    if config == 'testing':
        con=psycopg2.connect(test_url)
    return con
# def get_connection():
#         return psycopg2.connect(database=os.getenv('DATABASE'), 
#                                 user="afhewnyxybwlub", 
#                                 password="190cb34475295cddbf67b23f61f0b3fb60c7c4e7b24acc44cafdb7acd2982dd1",
#                                 host="ec2-54-83-38-174.compute-1.amazonaws.com",
#                                 port="5432")
# export DATABASE="dd3ga69u9o4v1h"

def init_DB():
        con = get_connection()
        return con


def create_tables():
        conn = get_connection()
        cur = conn.cursor()
        queries = tables()
        for query in queries:
                cur.execute(query)
        conn.commit()

def destroy_tables():
        users = """DROP TABLE IF EXISTS users CASCADE"""
        products = """DROP TABLE IF EXISTS products CASCADE"""
        sales = """DROP TABLE IF EXISTS sales CASCADE"""
        category = """DROP TABLE IF EXISTS category CASCADE"""
        tokens = """DROP TABLE IF EXISTS tokens CASCADE"""
        

        conn = get_connection()
        cur = conn.cursor()
        queries = [users, products, sales, category,tokens]
        for query in queries:
                cur.execute(query)
        conn.commit()

def tables():
        """Used for creating the tables"""
        users = """CREATE TABLE IF NOT EXISTS users(
                id serial PRIMARY KEY,
                username varchar (100) NOT NULL,
                email varchar(90) UNIQUE NOT NULL,
                password varchar(120) NOT NULL,
                role boolean NOT NULL)"""

        products = """CREATE TABLE IF NOT EXISTS products(
                id serial PRIMARY KEY,
                product_name varchar(100) UNIQUE NOT NULL,
                product_description varchar(255) NOT NULL,
                quantity int NOT NULL,
                price float(45) NOT NULL,
                category varchar(50) NOT NULL)"""

        
        sales = """CREATE TABLE IF NOT EXISTS sales (
                id serial PRIMARY KEY,
                sales_items varchar(200) NOT NULL,
                quantity int NOT NULL,
                price int NOT NULL)"""

        category = """CREATE TABLE IF NOT EXISTS category(
                id serial PRIMARY KEY,
                name varchar(50) UNIQUE NOT NULL)"""

        tokens = """CREATE TABLE IF NOT EXISTS tokens(
                id serial PRIMARY KEY,
                token varchar)"""

        tables = [users, products, category, sales, tokens]

        return tables

