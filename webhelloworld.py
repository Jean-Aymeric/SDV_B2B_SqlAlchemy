from flask import Flask, jsonify
import mysql.connector
app = Flask(__name__)

@app.route('/getAllDepartments', methods=['GET'])
def helloWorld():
    myDatabase = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="employees",
        port=3306
    )
    myCursor = myDatabase.cursor()
    myCursor.execute("SELECT * FROM departments;")

    myResult = myCursor.fetchall()
    records = []
    for record in myResult:
        records.append(record)
    myDatabase.close()
    return jsonify(records)

@app.route('/getDepartmentById/<string:id>', methods=['GET'])
def getDepartmentById(id):
    myDatabase = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="employees",
        port=3306
    )
    myCursor = myDatabase.cursor()
    myCursor.execute(f"SELECT * FROM departments WHERE departments.dept_no = '{id}';")

    myResult = myCursor.fetchall()
    records = []
    for record in myResult:
        records.append(record)
    myDatabase.close()
    return jsonify(records)

app.run(host='localhost', port=5000)