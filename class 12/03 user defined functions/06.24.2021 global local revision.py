#example 1
x='good'
def myfunction():
    x='excellent'
    print('programming is',x)   #programming is good
myfunction()
print('programming is',x)       #programming is excellent
#programming is excellent
#programming is good

#example 2
x='good'
def hello():
    global x
    x='excellent'
hello()
print('programming is', x)
#programming is excellent -as we have global variable

#example 3
c=0
def add():
    global c    #c value is throughout the program
    c+=2
    print(c)
add()
print(c)
#2
#2


