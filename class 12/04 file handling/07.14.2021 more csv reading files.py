#examaple 1
import csv
f=open('student.csv','r')
csv_reader=csv.reader(f)
for row in csv_reader:
    print(','.join(row))
f.close()
#roll no.,,
#1,rahul,45
#2,ragahav,23
#3,priya,11

#example 2
mytuple=('welcome','to','class12')
x='#'.join(mytuple)
print(x)
#   welcome#to#class12

#example3
dicti={'name':'akash','country':'swedan'}
sep='test'
x=sep.join(dicti)
print(x)
#nametestcountry

#example 4
import csv
f=open('student.csv','r')
csv_reader=csv.reader(f)
name=input('enter the name to be searched')
for row in csv_reader:
    if (row[0]==name):
        print(row)
#you have to input the roll number

#variation of example 4
f=open('student.csv','r')
csv_reader=csv.reader(f)
name=input('enter the name to be searched')
for row in csv_reader:
    if (row[1]==name):
        print(row)
#you have to input the name






























        

