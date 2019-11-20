from content import ContentDB
import logging

# import pdb
# pdb.set_trace()

logging.basicConfig(level=logging.DEBUG)

table_name = "emp"
cdb = ContentDB()
cdb.create_table(table_name, "contents")

# Insert some users into our database
try:
    cdb.add_entry(
        {
            "table": table_name,
            "staff_number": 22,
            "fname": "Rishabh",
            "lname": "Bansal",
            "gender": "M",
            "joining": "2014-03-28",
        }
    )
    # cdb.add_entry(table_name, 2, "Bill", "Gates", "M", "1980-10-28")
    cdb._commit()
except Exception:
    # print("Failed to add entries. %s", err)
    _ = 10
# Fetch the data

# print("Getting Entries.")
# print(cdb.get_entry(table_name))


# Store + print the fetched data
result = cdb._conn.cursor().fetchall()
# print(result)
for i in result:
    print(i)

""" Printed:
(1, 'Bill', 'Gates', 'M', '1980-10-28')
(23, 'Rishabh', 'Bansal', 'M', '2014-03-28')
"""

cdb.close()
