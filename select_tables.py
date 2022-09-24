import mysql.connector

select_tb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="143$mysqlmysql",
  database="firstdb"
)

st = select_tb.cursor()

st.execute("SELECT * FROM employees")

stresult= st.fetchall()

for i in stresult:
    print(i)