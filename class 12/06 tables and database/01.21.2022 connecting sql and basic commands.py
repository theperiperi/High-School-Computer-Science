import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',password='f1rewa11')
mycursor=mydb.cursor()
mycursor.execute('SHOW DATABASE')
for x in mycursor:
    print (x)

import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",passwd="f1rewa11")
mycursor=mydb.cursor()
mycursor.execute("CREATE DATABASE school")

import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',password='f1rewa11',database='school')
mycursor=mydb.cursor()
mycursor.execute('CREATE TABLE student (rollno int(3) primary key, name varchar(15),age integer(2), city char(8))')

import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",passwd="f1rewa11",database="school")
mycursor=mydb.cursor()
mycursor.execute("desc student")
for x in mycursor:
    print(x)
