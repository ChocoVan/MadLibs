import mysql.connector

my_db = mysql.connector.connect(
    host="localhost", 
    user="root",
    passwd="man-mylife-is-2-4ked",
)

my_cursor = my_db.cursor()

my_cursor.execute("CREATE DATABASE cards")

my_cursor.execute("SHOW DATABASES")
for db in my_cursor:
    print(db)