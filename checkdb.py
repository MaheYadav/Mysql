import mysql.connector

checkdb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="143$mysqlmysql"
)

check_databases = checkdb.cursor()

check_databases.execute("SHOW DATABASES")

for x in check_databases:
  print(x)
