import os
from psycopg2 import pool

connn_pool = pool.SimpleConnectionPool(
    1, 300,
    database=os.getenv('DB_NAME'),
    host=os.getenv('DB_HOST'),
    port=os.getenv('DB_PORT'),
    user=os.getenv('DB_USER'),
    password=os.getenv('DB_PASS')
    
)

class db:
  def __init__(self, table):
    self.table = table
    self.pool = connn_pool

  def insert(self,job_title,address,about_company,employement,roles_responsibilities,qualification,experience):
    conn = self.pool.getconn()
    cursor = conn.cursor()

    cursor.execute('INSERT INTO job_lisiting (job_title,address,about_company,employement,roles_responsibilities,qualification,experience) VALUES (%s,%s,%s,%s,%s,%s,%s)',(job_title,address,about_company,employement,roles_responsibilities,qualification,experience))
    conn.commit()

    conn.close() 

    return 201
  
  def select(self):
    conn = self.pool.getconn()
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM job_lisiting ORDER BY id DESC')

    rows = cursor.fetchall()

    conn.close()

    return rows