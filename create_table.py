import mysql.connector

createtable = mysql.connector.connect(
  host="localhost",
  user="root",
  password="143$mysqlmysql",
  database="firstdb"
)

ct = createtable.cursor()

ct.execute("CREATE TABLE Employees (Id int,name VARCHAR(255))")
print("Table is successfully created")