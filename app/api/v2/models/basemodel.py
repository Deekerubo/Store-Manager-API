import psycopg2
from psycopg2.extras import RealDictCursor
import os

# url="dbname=store_manager user=postgres password=nyambumo host=localhost"
# url="dbname=store_manager_tests user=postgres password=nyambumo host=localhost"
url="dbname=dd3ga69u9o4v1h user=afhewnyxybwlub password=190cb34475295cddbf67b23f61f0b3fb60c7c4e7b24acc44cafdb7acd2982dd1 host=ec2-54-83-38-174.compute-1.amazonaws.com"
class Basemodel():
    def __init__(self):
        self.conn = psycopg2.connect(url)
        self.cursor=self.conn.cursor(cursor_factory=RealDictCursor)
