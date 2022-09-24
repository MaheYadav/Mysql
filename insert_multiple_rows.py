import mysql.connector

insert_multiple_rows= mysql.connector.connect(
  host="localhost",
  user="root",
  password="143$mysqlmysql",
  database="firstdb"
)

imw = insert_multiple_rows.cursor()

emp = "INSERT INTO employees (ID, name) VALUES (%s, %s)"
empval = [
    (2,'Nag'),
    (3,'Raj'),
    (4,'Sai'),
    (5,'Rajesh'),
    (6,'Mahe'),
    (7,'Srinivas'),
    (8,'SiaRam'),
]

imw.executemany(emp, empval)

insert_multiple_rows.commit()

print(imw.rowcount, "was inserted.")