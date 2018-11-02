import psycopg2
from psycopg2.extras import RealDictCursor
import os


url=os.getenv('DATABASE_URL')
class Basemodel():
    def __init__(self):
        self.conn=psycopg2.connect(url)
        print(self.conn)
        self.cursor=self.conn.cursor(cursor_factory=RealDictCursor)
