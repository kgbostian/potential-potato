from content import ContentDB
import logging

logging.basicConfig(level=logging.DEBUG)
logging.debug("Debug")
logging.warning("Warning")

cdb = ContentDB()
cdb.create_table("emp","contents")

# Insert some users into our database
try:
  cdb._execute("""INSERT INTO emp VALUES (22, "Rishabh", "Bansal", "M", "2014-03-28");""")
  cdb._execute("""INSERT INTO emp VALUES (2, "Bill", "Gates", "M", "1980-10-28");""")
  cdb._commit()
except Exception as err:
  print("Failed to add entries. %s", err)
# Fetch the data 

cdb._connect_to_db()
print(cdb._conn.cursor().execute("SELECT name FROM sqlite_master WHERE type='table'").fetchall())
print(cdb._conn.cursor().fetchall())
# self._conn.cursor().execute("SELECT * FROM emp")

# Store + print the fetched data
result = cdb._conn.cursor().fetchall()
print(result)
for i in result:
  print(i)

""" Printed:
(1, 'Bill', 'Gates', 'M', '1980-10-28')
(23, 'Rishabh', 'Bansal', 'M', '2014-03-28')
"""

cdb.close()
