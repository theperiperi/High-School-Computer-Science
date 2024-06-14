#write csv
import csv
fields = ['Name', 'Branch', 'Year', 'CGPA']
st=open("university_records.csv",'w')
csvwriter = csv.writer(st) 
csvwriter.writerow(fields) 
st.close()
print('file created')

#append csv
import csv
List=[4,'William',5532,'10']              #text to be appended
st=open("university_records.csv",'a')#open file
write=csv.writer(st)                 #write in st   
write.writerow(List)                 #specifying what to write in st
st.close()
print('csv appended')

#read csv
import csv
f=open('shop.csv','r')
dt=csv.reader(f)
data=list(dt)
f.close()
print(data)
