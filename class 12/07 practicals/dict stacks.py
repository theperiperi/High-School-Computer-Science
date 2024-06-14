#dictionary stacks

#all function called through menu()

#push function 
def push():
    name=input('enter the name of the player')
    runs=int(input('enter the number of run'))
    score={'kapil':40,'sachin':55,'saurav':80,'rahul':35,'yuvraj':110}
    #gets appended to dictionary
    score[name]=runs
    global stack
    stack=[]
    for ele in score:
        if score[ele]>49:
            stack.append(ele)
    menu()

#pop function
def pop():
    stack.pop()
    menu()

#printing the stack at the present stage
def display():
    print(stack)
    menu()

#function to make the program menu driven
#call all function within menu()
def menu():
    choice=int(input('enter choice \n1.push\n2.pop\n3.display\n4.end program'))
    if choice==1:
        push()
    if choice==2:
        pop()
    if choice==3:
        display()
    if choice==4:
        print('program ended')

menu()

