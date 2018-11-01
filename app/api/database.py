# #Cretate a Database connection
import psycopg2
import os

url = os.getenv('DATABASE_URL')
def get_connection(url):
    con = psycopg2.connect(url)
    
    return con

def init_db():
    con = get_connection(url)
    print(con)
    return con

def create_tables():
    conn = get_connection(url)
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
    
def tables():
        """Used for creating the tables"""
        users = """CREATE TABLE IF NOT EXISTS users(
                id serial PRIMARY KEY,
                username varchar (20) NOT NULL,
                email varchar(90) UNIQUE NOT NULL,
                password varchar(120) NOT NULL,
                role float(1) NOT NULL)"""

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

