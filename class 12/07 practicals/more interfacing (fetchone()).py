import mysql.connector
connection=mysql.connector.connect(host='localhost',user='root',password='f1rewa11',database='boards')
cursor=connection.cursor()
query='select * from book'
x=cursor.execute(query)

cursor.fetchone()
print(cursor.rowcount)

