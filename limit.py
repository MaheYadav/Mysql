import mysql.connector

limit_rows = mysql.connector.connect(
  host="localhost",
  user="root",
  password="143$mysqlmysql",
  database="firstdb"
)

limit_rows_cursor = limit_rows.cursor()

limit_rows_cursor.execute("SELECT * FROM employees LIMIT 5")

limitresult = limit_rows_cursor.fetchall()

for i in limitresult:
  print(i)