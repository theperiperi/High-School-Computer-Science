#push and pop operations for the following fxns
#insertion of items into a stack insert()
#delettion of items in stack Delete()
#employee name and designation
s=[]
c='y'
while(c=='y'):
    print('1.push')
    print('2.pop')
    print('3.display')
    choice=int(input('enter your choice:'))

    #push block
    if choice==1:
        def insert():
            a=input('employee name:')
            b=input('employee designation:')
            c=a+' '+b
            s.append(c)
        insert()

    elif(choice==2):
        def Delete():
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



