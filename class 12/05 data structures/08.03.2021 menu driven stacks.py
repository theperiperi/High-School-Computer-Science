#menu driven program: stacks

s=[]
c='y'
while(c=='y'):
    print('1.push')
    print('2.pop')
    print('3.display')
    choice=int(input('enter your choice:'))
    if choice==1:
        a=input('enter any number:')
        s.append(a)
    elif(choice==2):
        if(s==[]):
            print('stack is empty') #underflow
        else:
            print('deleted element is:',s.pop())

    elif(choice==3):
        l=len(s)
        for i in range(l-1,-1,-1): #display elements from last to first
            print(s[i])

    else:
        print('wrong input')
    c=input('do you want to continue or not')
