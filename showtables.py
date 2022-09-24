import mysql.connector

showtables= mysql.connector.connect(
  host="localhost",
  user="root",
  password="143$mysqlmysql",
  database="firstdb"
)

st = showtables.cursor()

st.execute("SHOW TABLES")
print("Showing tables  form firstdb")
for x in st:
     print(x)
