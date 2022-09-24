import mysql.connector

conn = mysql.connector.connect(
  host="localhost",
  user="Mahi",
  password="143$mysqlmysql"
)
if conn.is_connected():
  print("Connection is Established")