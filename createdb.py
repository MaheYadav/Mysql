import mysql.connector

firstdb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="143$mysqlmysql"
)

dbcreated = firstdb.cursor()

dbcreated.execute("CREATE DATABASE firstdb")
print("Database is Successfully created")


#If this page is executed with no error, you have successfully created a database.
