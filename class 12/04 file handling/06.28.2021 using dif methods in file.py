#program to read only first 10 characters of the file
f=open('06.28.2021 test1.txt','r')
#'r' means read mode
#calling external .txt file
data=f.read(10)
#number of characters to print=10
print(data)
#mic testin     #1st 10 char of mic testing
f.close()   #works without this line
#but the line is mandatory


#Readline() method:
#the readline() method will return a line red as a string from the file
#syntax:
#fileobject.readline()
#print(file.readline())

f=open('06.28.2021 test2.txt','r')
line1=f.readline()
print(line1,end='')
#python
line2=f.readline()
print(line2,end='')
#computer
line3=f.readline()
print(line3,end='')
#science

#readline gives output as string
#read just takes as such
