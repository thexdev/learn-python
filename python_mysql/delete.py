from config.db import db
from config.db import cursor

sql       = 'DELETE FROM modules WHERE id = %s'
module_id = (4,)

cursor.execute(sql, module_id)
db.commit()

print('{effected_row} record(s) deleted!'.format(effected_row = cursor.rowcount))