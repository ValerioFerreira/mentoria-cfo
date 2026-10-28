import psycopg2
from dotenv import dotenv_values

cfg = dotenv_values('web/.env')
url = cfg.get('DATABASE_URL')
conn = psycopg2.connect(url)
cur = conn.cursor()
cur.execute('SELECT batch, kind, count(*) FROM "Question" GROUP BY batch, kind ORDER BY count(*) DESC')
for row in cur.fetchall():
    print(row)
cur.close()
conn.close()
