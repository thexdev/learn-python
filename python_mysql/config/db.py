from mysql import connector

db = connector.connect(
	host     = 'localhost',
	user     = 'root',
	passwd   = 'Axeone@dev2503',
	database = 'python'
)

cursor = db.cursor()