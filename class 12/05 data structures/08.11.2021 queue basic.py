#write a program to add delete and display elements from a cue
#FIFO
a=[]
c='y'
while(c=='y'):
    print('1.insert')
    print('2.delete')
    print('3.display')
    choice=int(input('enter you choice'))
    
    if choice==1:
        b=int(input('enter the number'))
        a.append(b)
        
    elif(choice==2):
        if(a==[]):
            print('queue empty')
        else:
            print('deleted element is',a[0])
            a.pop(0)
            
    elif choice==3:
        l=len(a)
        for i in range (0,l):
            print(a[i])
    else:
        print('wrong choice')
    c=input('do you want to continue or not')
    












































