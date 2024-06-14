#example 1
import csv
with open ('student.csv','r') as csvfile:
    reader=csv.reader(csvfile)
    for row in reader:
        print(row)

#example 2
import csv
with open ('student.csv','r') as csv_file:
    reader =csv.reader(csv_file)
    rows=[]
    for rec in reader:
        rows.append(rec)
    print(rows)

#example 3
import csv
f=open('student.csv','r')
csv_reader=csv.reader(f)
coloumns=next(csv_reader)
c=0
#reading record by record
for row in csv_reader:
    c+=1
print('no of records:',c)
f.close()
