from config.db import db
from config.db import cursor

sql = 'DROP TABLE IF EXISTS language';

cursor.execute(sql)
db.commit()

print(cursor.rowcount)