import csv
def addcsvfile(username,password): #to write data in csv file
    f=open('mydata.csv','a')
    newfilewriter=csv.writer(f)
    newfilewriter.writerow([username,password])
    f.close() #csv file reading code
def readcsvfile(): #to read data from csv file
    with open('mydata.csv','r') as newfile:
        newfilereader=csv.reader(newfile)
    for row in newfilereader:
        print(row[0],row[1])
newfile.close()
addcsvfile("aman",'123@456')
addcsvfile("anis",'aru@nima')
addcsvfile("raju",'myname@fri')
readcsvfile()
            
#board exam incorrect question
