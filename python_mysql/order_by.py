from config.db import cursor

sql = 'SELECT * FROM modules ORDER BY name DESC';

cursor.execute(sql)

for record in cursor.fetchall() :
	print(record)