import mysql.connector



mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="new_password",
    database="db1"
)
mycursor = mydb.cursor()

sql = """INSERT INTO customers
            VALUES (%s, %s)"""
val = 'dddd'
val2 = 'ddddr'

mycursor.execute(sql, val, val2)

mydb.commit()

print("1 record inserted, ID:", mycursor.lastrowid)



#mycursor.execute("SELECT * FROM employees")

#myresult = mycursor.fetchall()

#for x in myresult:
 # print(x)


#print(mydb)

#mycursor = mydb.cursor()

#sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
#val = ("John", "Highway 21")
#mycursor.execute(sql, val)

#mydb.commit()

#print(mycursor.rowcount, "record inserted.")




#mycursor.execute("SHOW TABLES")
#sql = "INSERT INTO employees(index, first_name, last_name, personal_id, departmant) VALUES(%d, %s, %s, %s, %s)"
#dat = (3, 'dgdgd', 'fdfd','dfsd','fss',)

#mycursor.execute("SELECT * FROM employees")

#mycursor.executemany(sql, dat)

#mycursor.execute(""""INSERT INTO employees(index, first_name, last_name, personal_id, departmant) VALUES(%d, %s, %s, %s, %s)""", (3, 'dgdgd', 'fdfd','dfsd','fss'))

#for tb in mycursor:
 #   print(tb)

