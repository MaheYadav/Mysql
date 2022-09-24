import mysql.connector

insert_table = mysql.connector.connect(
  host="localhost",
  user="root",
  password="143$mysqlmysql",
  database="firstdb"
)

it = insert_table.cursor()

emp = "INSERT INTO  employees (Id, name) VALUES (%s, %s)"
empval = ( "1","Mahendra",)
it.execute(emp, empval)
insert_table.commit()

print(it.rowcount, "record inserted.")