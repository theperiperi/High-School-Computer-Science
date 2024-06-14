#Write a function in Python PUSH(Arr), where Arr is a list of numbers.
#From this list push all numbers divisible by 5 into a stack implemented by
#using a list. Display the stack if it has at least one element,
#otherwise display appropriate error messages

arr=eval(input('enter a list'))
s=[]
def push(arr):
    for ele in arr:
        if ele%5==0:
            s.append(ele)
    print(s)
    if len(s)==[]:
        print('error')
push(arr)
            
