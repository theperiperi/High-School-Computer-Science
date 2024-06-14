#Write a program to implement stack for the book details such as book number and book name. Each item node of stack has 2 elements, book number and name.
#Implement push and display operations
s=[]
c='y'
while(c=='y'):
    print('1.push')
    print('2.display')
    choice=int(input('enter your choice:'))

    #push block
    if choice==1:
        a=input('enter book number:')
        b=input('enter book name:')
        c=a+' '+b
        s.append(c)

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


#Write a function add(books) and delete(books), to add and remove books, considering them to act as append and pop operation in stack.
    
s=[]
edit='y'

while edit=='y':
    book=input('enter book name')
    #defining function
    def add(book):
        s.append(book)
    def delete(book):
        s.remove(book)

    #the function calls
    option=input('user do you wish to add or delete this book?')
    if option=='add':
        add(book)
    if option=='delete':
        delete(book)

    edit=input('do you wish to continue editting?')
    
print(s)


#List the two ways to implement stack
#push and pop

    

