from mysql import connector

db = connector.connect(
	host     = 'localhost',
	user     = 'root',
	passwd   = 'Axeone@dev2503',
	database = 'python'
)

cursor = db.cursor()
cursor.execute('SELECT * FROM modules')

for record in cursor.fetchall() :
	for item in record :
		print(item)