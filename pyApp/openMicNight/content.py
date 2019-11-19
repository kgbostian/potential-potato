import sqlite3
import logging
import inspect

logging.basicConfig(level=logging.INFO)


class ContentDB:
    def __init__(self, db_name="database.db"):
        self._db_name = db_name
        self._connect_to_db()
        self._logger = logging.getLogger(__name__)

    def _commit(self):
        self.log_entry()
        self._conn.commit()
        self.log_entry("Leaving")
        return None

    def _connect_to_db(self):
        self._conn = sqlite3.connect(self._db_name)
        self._c = self._conn.cursor()
        # self.log_entry()
        # self.log_entry("Leaving")
        return None

    def cc(self):
        self.log_entry()
        self._conn.commit()
        self._conn.close()
        self.log_entry("Leaving")
        return None

    def _debugPrint(self):
        self.log_entry()
        data = self._c.execute("SELECT * FROM emp").fetchall()
        self.log_entry("Leaving")
        return data

    def _execute(self, statement):
        try:
            self.log_entry()
            self._logger.debug(f"Statement to be executed: {statement}")
            self._c.execute(statement)
            self._logger.debug(f"debug print: {self._debugPrint()}")
            self.log_entry("Leaving")
        except TypeError as error:
            self._logger.debug("Failed to execute statement. %s", error)
            raise error

    """
    Create a table with table_name and header listed in table_contents.
    param: table_name      Name of table
           table contents  List of dictionaries describing the schema.
    """

    def create_table(self, table_name, table_contents=""):
        SQL_STATEMENT = """CREATE TABLE IF NOT EXISTS {} (
          staff_number INTEGER PRIMARY KEY,
          fname VARCHAR(20),
          lname VARCHAR(30),
          gender CHAR(1),
          joining DATE
        );""".format(
            table_name
        )
        # self._logger.debug(SQL_STATEMENT)
        self._execute(SQL_STATEMENT)
        self._commit()

    # Add santization of data in private helper to
    # build the complex dictionary.
    ###
    ###
    #  def

    def add_entry(self, data):
        try:
            SQL_STATEMENT = (
                f"INSERT INTO {data['table']} VALUES"
                + f" ({data['staff_number']},"
                + f" '{data['fname']}', '{data['lname']}', "
                + f"'M', '2014-03-28');"
            )
            # self._logger.debug(f"Adding Entry: {SQL_STATEMENT}")
            self._execute(SQL_STATEMENT)
            self._commit()
            return None
        except Exception as err:
            raise err

    def get_entry(self, tbl, sID=None):
        self.log_entry()
        self._logger.debug(f"Getting entry {sID}")
        try:
            if sID:
                SQL_STATEMENT = f"SELECT * from {tbl} WHERE staff_number={sID};" # noqa
            else:
                SQL_STATEMENT = f"SELECT * from {tbl};"
            self._execute(SQL_STATEMENT)
            data = self._conn.cursor().fetchall()
            self._logger.debug(f"Data from select: {data}")
            self.log_entry("Leaving")
            return data
        except Exception as err:
            self._logger.error(f"Failed to get entry: {err}")
            raise Exception

    def close(self):
        self._conn.close()

    def log_entry(self, prelude="Entering "):
        self._logger.debug(f"{prelude} {inspect.stack()[1].function}")
