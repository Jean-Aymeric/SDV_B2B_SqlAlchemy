import mysql.connector

myDatabase = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="helloworld",
    port=3306
)

myCursor = myDatabase.cursor()
myCursor.execute("SELECT * FROM helloworld;")

myResult = myCursor.fetchall()
for record in myResult:
    print(record)
myDatabase.close()