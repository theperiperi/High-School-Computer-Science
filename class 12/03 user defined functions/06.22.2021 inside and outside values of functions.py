x=int(input('enter base'))
y=int(input('enter expo'))
z=0
def expo(x):
   z=x**y
   print(z)
expo(x)

#a variable that can be accessed only within the function or block in which
#it is created. when a particular variable which is created inside a function
#or block, the variable is said to be local on it. a local variable exists only
#while the function is executing.

#example 1
a=570
b=20
def test():
    print('value of a is',a,'b is',b)

print('value of a is',a,'b is',b)
test()
#value of a is 570 b is 20
#value of a is 570 b is 20

#example 2
a=570
def test2():
    a=57
    b=27
    print('value of a and b inside function are',a,b)
print('value of a outside function is:',a)

#example 3
a=570
def test():
    global a
    a=5
    b=5
    print('value of a and b inside the function are',a,b)
    print('value of an outside function is',a)
test()
#5,5
#5

#alternative example 
a=570
def test():
    global a
    a=5
    b=5
    print('value of a and b inside the function are',a,b)
test()
print('value of an outside function is',a)
#5,5
#5

