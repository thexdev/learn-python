from mysql import connector

db = connector.connect(
	host   = 'localhost',
	user   = 'root',
	passwd = 'Axeone@dev2503'
)

if db :
	print('Database is connected!')
else :
	print('Database not connected!')