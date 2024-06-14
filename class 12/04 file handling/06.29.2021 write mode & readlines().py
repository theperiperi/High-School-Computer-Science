#program to read data from 2nd character into list
f=open('06.28.2021 test2.txt','r')
print(f.read(2))
print(f.readlines())
print('reamaining data')
print(f.read(5))

#py
#['thon\n', 'computer\n', 'science']
#reamaining data


#program to read all lines into a list (including(readlines())
f=open('06.28.2021 test2.txt','r')
lines=f.readlines()
for line in lines:
    print(line,end='')
f.close()

#python
#computer
#science

#example for write and read
x=['have\n','nice\n','day\n']
#writing into file
file1=open('06.29.2021 test1.txt','w')
#'w' write mode:creates file
file1.writelines((x))
file1.close()
#we created a new text file!

file=open('06.29.2021 test1.txt','r')
count=0
while True:
    count+=1
    #get next line from file
    line=file.readline()
    if not line:
        break
    print('line{}:{}'.format(count,line.strip()))
    #scienceline1:have
    #line2:nice
    #line3:day
file.close()

#another write program
f=open('06.29.2021 test2.txt','w')
list=['csc\n','eng\n','phy\n','chem\n','mat\n']
f.writelines(list)
print('tex file successfully created')
f.close()

























    



