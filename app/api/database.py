# #Cretate a Database connection
import psycopg2
import os

url = "host='localhost' port='5432' user='postgres' dbname='store_manager' password='nyambumo'"
# db_url = os.getenv('DATABASE_URL')
def get_connection(url):
    con = psycopg2.connect(url)
    # print(con)
    return con

def init_db():
    con = get_connection(url)
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
    pass
def tables():
        """Used for creating the tables"""
        users = """CREATE TABLE IF NOT EXISTS users (
                user_id serial PRIMARY KEY,
                email varchar(90) UNIQUE NOT NULL,
                passsword varchar(120) NOT NULL,
                registered_on varchar(100) NOT NULL)"""

        products = """CREATE TABLE IF NOT EXISTS products(
                prod_id serial PRIMARY KEY,
                product_name varchar(100) UNIQUE NOT NULL,
                product_description varchar(255) NOT NULL,
                quantity int NOT NULL,
                price float(45) NOT NULL,
                category varchar(50) NOT NULL)"""

        sales = """CREATE TABLE IF NOT EXISTS sales (
                sales_id serial PRIMARY KEY,
                sales_items varchar(200) NOT NULL,
                quantity int NOT NULL,
                price int NOT NULL)"""

        tables = [users, products, sales]

        return tables
