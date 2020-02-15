
from flask import Flask, render_template, json, request, redirect
import mysql.connector


app = Flask(__name__)

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="new_password",
    database="db1"
)

mycursor = mydb.cursor()

@app.route('/', methods=['POST', 'GET'])
def main():
        mycursor.execute("SELECT * FROM employees")
        fetchall = mycursor.fetchall()

        return render_template('index.html', data = fetchall)


@app.route('/showSignUp', methods=['POST', 'GET'])
def showSignUp():

    if request.method == 'POST':
        #index = request.form['inputIndex']
        #lname = request.form['inputFName']
        #fname = request.form['inputLName']
        #idname = request.form['inputID']
        #depname = request.form['inputDepartment']
        sql = """INSERT INTO employees
                    VALUES (5,'rty', 'rfdc', 'bxd', 'fdcdx')"""
        mycursor.execute(sql)
        mydb.commit()

    return render_template('signup.html')

@app.route('/showSignIn', methods=['POST', 'GET'])
def showSignIn():
    if request.method == 'POST':
         sql = "UPDATE employees SET first_name = %s WHERE last_name = %s"
         val = ("eerff", "eee")
         mycursor.execute(sql,val)
         mydb.commit()
    return render_template('signup.html')


if __name__ == '__main__':
	app.run()