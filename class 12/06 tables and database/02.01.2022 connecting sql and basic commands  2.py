import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",passwd="f1rewa11",database="school")
mycursor=mydb.cursor()

#for table display
mycursor.execute("select * from student")
myrecords=mycursor.fetchall()
for x in myrecords:
    print(x)

#for displayof particular fields
mycursor.execute("select name, age from student where city='Chennai'")
myrecords=mycursor.fetchall()
for x in myrecords:
    print(x)

#for row deletion
mycursor.execute("delete from student where rollno=1")
mydb.commit()
print(mycursor.rowcount,"Record deleted")

