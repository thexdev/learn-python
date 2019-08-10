from config.db import db
from config.db import cursor

sql = 'SELECT * FROM modules LIMIT 2 OFFSET 1'

cursor.execute(sql)

for record in cursor.fetchall() :
	print(record)