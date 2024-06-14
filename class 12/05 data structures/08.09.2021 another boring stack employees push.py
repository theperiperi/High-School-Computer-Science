#program to add, delete and display records of employee
#using list implementation through stack

s=[]
c='y'
while(c=='y'):
    print('1.push')
    print('2.pop')
    print('3.display')
    choice=int(input('enter your choice:'))

    #push block
    if choice==1:
        a=input('employee id:')
        b=input('employee name:')
        c=a+' '+b
        s.append(c)

    elif(choice==2):
        if(s==[]):
            print('stack is empty') #underflow
        else:
            print('deleted element is:',s.pop())

    #display block
    elif(choice==3):
        l=len(s)
        for i in range(l-1,-1,-1): #display elements from last to first
            print(s[i])
            #mod to display index
            #print(i)

    #control of program flow
    else:
        print('wrong input')
    c=input('do you want to continue or not')
