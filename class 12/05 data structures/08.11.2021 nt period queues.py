#cities
city=input('enter city')
s=[]
def push(city):
    s.append(city)
    print(s)
push(city)

def pop(city):
        print('the deleted element is',s.pop(0))
pop(city)

#write a fxn for insertion and deletion operation to remove a number from a list of numbers
#push(num), pop(num)s=[]
num=eval(input('enter list'))
s=[]
def push(num):
    s.append(num)
    print(s)
push(num)

def pop(num):
        print('the deleted element is',s.pop(0))
pop(num)


