#writing a csv file
import csv
fields=['name','class','year','percent'] #columns
rows= [
      ['rohit','12','2003','92'],
      ['deepak','12','2006','52'],
      ['sam','12','2005','95'],
      ['kaushik','12','2006','90'] #records
      ]
filename='marks.csv' #create a file
with open(filename,'w',newline='')as f:
    csv_w=csv.writer(f,delimiter=',')
    csv_w.writerows(fields)
    for i in rows:
        csv_w.writerow(i)
    print('file created')
