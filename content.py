import sqlite3

class ContentDB:
  db_name = "database.db"
  conn = ""

  def commit(self):
    self.conn.commit()

  def connect_to_db(self):
    self.conn = sqlite3.connect(self.db_name)
    self.c = self.conn.cursor()

  def cc(self):
    self.conn.commit()
    self.conn.close()

  def table_exists(self, c, table_name):
    #SQLStatement = "SELECT name FROM sqlite_master WHERE type='table' AND name='%s';".format(table_name) 
    SQLStatement = "SELECT count(name) FROM sqlite_master WHERE type='table' AND name='emp';"
    self.c.execute(SQLStatement)

    try:
      if(self.c.fetchone()[0] == 1):
        return True
      else:
        return False
    except (TypeError) as err:
        return False 


  '''
  Create a table with table_name and header listed in table_contents.
  param: table_name      Name of table
         table contents  List of dictionaries describing                   the schema.
  '''
  def create_table(self, table_name, table_contents=""):
    SQL_STATEMENT = """CREATE TABLE IF NOT EXISTS {} (
      staff_number INTEGER PRIMARY KEY,
      fname VARCHAR(20),
      lname VARCHAR(30),
      gender CHAR(1),
      joining DATE
    );""".format(table_name)
    # logger.debug(SQL_STATEMENT)

    if(self.table_exists(self.c, table_name)):
      self.commit()
      # logger.debug("Table {} exists".format(table_name))
    else:
      self.c.execute(SQL_STATEMENT)
      self.commit()
      # logger.debug("Created table {}.".format(table_name))

  def rest_of_stuff(self):
    #self.connect_to_db()
    # Insert some users into our database
    try:
      self.conn.cursor().execute("""INSERT INTO emp VALUES (23, "Rishabh", "Bansal", "M", "2014-03-28");""")
      self.conn.cursor().execute("""INSERT INTO emp VALUES (1, "Bill", "Gates", "M", "1980-10-28");""")
      self.commit()
    except sqlite3.IntegrityError:
      print("Failed to add entries.")
    # Fetch the data 
    
    self.conn.cursor().execute("SELECT name FROM sqlite_master WHERE type='table'")
    print(self.conn.cursor().fetchall())
    # self.conn.cursor().execute("SELECT * FROM emp")

    # Store + print the fetched data
    result = self.conn.cursor().fetchall()
    print(result)
    for i in result:
      print(i)

    """ Printed:
    (1, 'Bill', 'Gates', 'M', '1980-10-28')
    (23, 'Rishabh', 'Bansal', 'M', '2014-03-28')
    """

    # Remember to save + close
    self.commit()
    self.conn.close()
