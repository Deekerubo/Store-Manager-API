import psycopg2
from psycopg2.extras import RealDictCursor
import os


url="dbname=store_manager_tests user=postgres password=nyambumo host=localhost"
class Basemodel():
    def __init__(self):
        self.conn = psycopg2.connect(url)
        self.cursor=self.conn.cursor(cursor_factory=RealDictCursor)
