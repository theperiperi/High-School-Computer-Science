#declaration for list implemented stack
stack=list()
#function to pop a number from the stack
def pop(stack,top):
    if not stack:
        print('stack is empty')
    else:
        num=stack.pop() #removing top elementsfrom the stack
        top-=1
    print('value denoted from stack is',num)
    return top
pop([1,2,3,4],3)
pop('1,2,3,4',3) 

