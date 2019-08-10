from mysql import connector

db = connector.connect(
	host     = 'localhost',
	user     = 'root',
	passwd   = 'Axeone@dev2503',
	database = 'python'
)

cursor = db.cursor()

sql = 'INSERT INTO modules (name, syntax) VALUES (%s, %s)'
val = ('datetime', 'from datetime import datetime')

cursor.execute(sql, val)
db.commit()

print('{inserted_record} Record(s) inserted, ID: {ID}'.format(inserted_record = cursor.rowcount, ID = cursor.lastrowid))