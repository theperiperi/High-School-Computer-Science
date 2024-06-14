#writing numeric data into a file
f=open('06.30.2021 test1.txt','w')
#this also works as a doc file
x=100
f.write('hello world\n')
f.write(str(x))#numeric value is string
print('file created')
f.close()

#output in '06.30.2021 test1.txt'
#hello world
#100


with open('06.30.2021 test2.txt','w') as f:
#basically means:  f=('06.30.2021 test2.txt','w')
    f.write('python\n')
    f.write('is an easy\n')
    f.write('language\n')
    f.write('to work with\n')
    print('is file closed:',f.closed)
    f.close()#False
    #f.closed: checks if closed or not (True/False)
    
#variation
with open('06.30.2021 test2.txt','w') as f:
    f.write('python\n')
    f.write('is an easy\n')
    f.write('language\n')
    f.write('to work with\n')
    f.close()
    print('is file closed:',f.closed)#True
    
