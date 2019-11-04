from content import ContentDB

cdb = ContentDB()
cdb.connect_to_db()
cdb.create_table("emp","contents")
cdb.rest_of_stuff()
