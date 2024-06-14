
setup={'hr':10,'quality':25,'support':50,'production':20,'supply':25}
def push():
    global stack
    stack=[]
    for ele in setup:
        if setup[ele]>=25:
            stack.append(ele)
    print(stack)

def pop():
    stack.pop()
    print(stack)
    
push()
pop()

        
