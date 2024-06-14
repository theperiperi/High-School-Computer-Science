#write a program to add remove and display book details as a que (book id, name)
x=[]
c='y'
while (c=='y'):
    print('1.insert')
    print('2.delete')
    print('3.display')
    choice=int(input('enter your choice'))

    if choice==1:
        a=int(input('enter book number'))
        b=input('enter book name')
        #y=(a,b)#tuple created for new book
        a=str(a)
        y=a+' '+b
        x.append(y)

    elif choice==2:
        if x==[]:
            print('queue is empty')
        else:
            print('the deleted element is',x.pop(0))

    elif choice==3:
        l=len(x)
        for i in range(0,l):
            print(x[i])

    else:
        print('wrong choice')
    c=input('do you want to continue')
