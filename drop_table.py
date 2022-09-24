import mysql.connector

drop_table = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="firstdb"
)

mycursor = drop_table.cursor()

sql = "DROP TABLE employees"

mycursor.execute(sql)