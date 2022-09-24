import mysql.connector
# you can try to access the database when making the connection:
# Try connecting to the database "mydatabase":
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="143$mysqlmysql",
  database="firstdb"
)
print("Connection makes successful")
