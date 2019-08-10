from config.db import db
from config.db import cursor

sql = 'UPDATE modules SET name = %s, syntax = %s WHERE id = %s'
val = ('platform', 'import platform', 6)

cursor.execute(sql, val)
db.commit()

print('{affected_row} record(s) affected!'.format(affected_row = cursor.rowcount))