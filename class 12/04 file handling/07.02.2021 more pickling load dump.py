#pickle load
import pickle
f=open('07.01.2021 test2.dat','rb')
dict1=pickle.load(f)#reading file from binary file
f.close()
print(dict1)
#{'python': 85, 'java': 76, 'c++': 80, 'jsp': 65}

#program to store multiple integers in a binary file and print
def binfile():
    import pickle
    file=open('07.02.2021 test1.dat','wb')
    while True:
        x=int(input('enter the integer:'))
        pickle.dump(x,file)
        a=input('do you want to enter more data? (Y/N)')
        if a.upper()=='N':break
    file.close()
    file=open('07.02.2021 test1.dat','rb')
    try:
        while True:
            y=pickle.load(file)
            print(y)
    except EOFError:
        pass
    file.close()
binfile()
#but some stuff here aren't in portions
#remark: basically program doesn't work because instead of y/n if we put integer
#also it works

#program to take input for student details
import pickle
#function definition
def writedetails():
    lst=[]
    while True:
        r=int(input('enter the roll number'))
        n=input('enter name')
        p=float(input('enter the %'))
        d=str(r)+' '+n+' '+str(p)
        lst.append(d)
        ch=input('wish to add more records(y/n)')
        if(ch=='y' or ch=='Y'):
            continue
        else:
            break
    fp=open('07.02.2021 test2.dat','wb')
    pickle.dump(lst,fp)
    print('executed')
    fp.close()
writedetails()
