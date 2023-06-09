import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database = "mydatabase"
)

mycursor = mydb.cursor ()
mycursor.execute("CREATE TABLE customers (name VARCHAR (255), address VARCHAR (255))")
sql = "INSERT INTO customers (name, address) VALUES (%, %)"
val = ("John", "Highway 21")
mycursor.execute(sql, val)

mydb.commit()
print(mycursor.rowcount, "record inserted.")