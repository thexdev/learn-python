from mysql import connector

db = connector.connect(
	host     = 'localhost',
	user     = 'root',
	passwd   = 'Axeone@dev2503',
	database = 'python'
)

cursor = db.cursor()
cursor.execute('CREATE TABLE modules (name VARCHAR(125), call_systax VARCHAR(125))')

if cursor :
	print('Query successfully executed!')
else :
	print('Query failed to execute!')