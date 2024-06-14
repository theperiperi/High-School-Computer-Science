#practicals code b
n=[3,5,10,13,21,23,45,56,60,78]
stk=[]
def push():
    for ele in n:
        if ele%3==0:
            stk.append(ele)
    print(stk)

def pop():
    stk.pop()
    print(stk)
    
push()
pop()
