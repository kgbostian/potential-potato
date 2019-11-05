import sqlite3
import logging


class ContentDB:

  def __init__(self, db_name="database.db"):
    self._db_name = db_name
    self._connect_to_db()
    self._logger = logging.getLogger(__name__)

  def _commit(self):
    self._conn.commit()

  def _connect_to_db(self):
    self._conn = sqlite3.connect(self._db_name)
    self._c = self._conn.cursor()

  def cc(self):
    self._conn.commit()
    self._conn.close()

  def _debugPrint(self):
    self._logger.debug(self._conn.cursor().execute("SELECT * FROM emp").fetchall())

  def _execute(self, statement):
    try:
        self._c.execute(statement)
        self._commit()
        self._debugPrint()
    except TypeError as error:
        self._logger.debug("Failed to execute statement. %s", err)
        raise Execution


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
    self._logger.debug(SQL_STATEMENT)
    self._execute(SQL_STATEMENT)
        

  def close(self):
    self._conn.close()
