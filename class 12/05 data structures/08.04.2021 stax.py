#write a function to perform push operations on a stack containing student
#details as given in the following definition of student node
#parameters:roll numbers(int), name(str), age(int)

stk=[]
def isEmpty(stk):
    if stk==[]:
        return True
    else:
        return False
def stk_push(stk, item):
    stk.append(item)
    top=len(stk)-1
    print(stk)   
isEmpty(stk)
stk_push(stk)

    

#same program for pop
def stkpop(stk):
    if isEmpty():
        print("Underflow")
    else:
        item=stk.pop()
        print(item)
    if len(stk)==0:
        top=None
    else:
        top=len(stk)-1
