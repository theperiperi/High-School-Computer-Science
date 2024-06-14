import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",passwd="f1rewa11",database="school")
mycursor=mydb.cursor()
mycursor.execute("UPDATE student set age=28 where name='Pooja'" )
mydb.commit()
print(mycursor.rowcount,"Record updated")

import mysql.connector
db1=mysql.connector.connect(host="localhost",user="root",passwd="f1rewa11",database="school")
mycursor=db1.cursor()
nm=input("Enter name of the student whose record is to be deleted")
#to delete records
try:
    mycursor.execute("DELETE FROM STUDENT WHERE ame='nm')" )
    print(mycursor.rowcount,"deleted")
    db1.commit()
except:
    db1.rollback()
    db1.close()
