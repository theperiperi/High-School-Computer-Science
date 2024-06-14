#program for stack name,roll number, age
s=[]
c='y'
while(c=='y'):
    print('1.push')
    print('2.display')
    choice=int(input('enter your choice:'))

    #push block
    if choice==1:
        a=input('name:')
        b=int(input('roll number:'))
        c=int(input('age'))
        b=str(b)
        c=str(c)
        d=a+' '+(b)+ ' '+(c)
        s.append(d)

    #display block
    elif(choice==2):
        l=len(s)
        for i in range(l-1,-1,-1): #display elements from last to first
            print(s[i])
            #mod to display index
            #print(i)

    #control of program flow
    else:
        print('wrong input')
    c=input('do you want to continue or not')

