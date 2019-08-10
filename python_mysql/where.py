from config.db import cursor

sql        = "SELECT * FROM modules WHERE id = %s"
modules_id = (1,)

cursor.execute(sql, modules_id)

for record in cursor :
	print(record)