#scope of a variable is defined as the lifetime of a variable'
#local variable program:
def fun():
    s='i love india!' #local variable
    print(s)
s='i love world'
fun()
print(s)
#output
#i love india!
#i love world

#global variable program
def fun():
    global s#accessing/making global variable for fun()
    print(s)    #this prints world
    s='i love india'
    print(s)    #this prints india
s='i love world'#here it still takes as i love india as india is global
fun()
print(s)        #this prints india
#output:
#i love world
#i love india
#i love india

#global program (another one)
def f():
    global s
    print(s) #python
    s='class 12 computer science'
    print(s) #class12
#global scope
s='python programming'
f()
print(s)     #class12

#another global program
z=25
def func():
    global z
    print(z)#25
    z=20
func()
print(z)#20

#variation of above pgm
z=25
def func():
    global z
    print(z)#20
z=20
func()
print(z)#20

#global
def func(x,y):
    a=45
    x,y=y,x
    b=33
    b=17
    print(a,b,x,y)
a,b,x,y=3,15,3,4
func(9,81)
print(a,b,x,y)
#45 17 81 9
#3 15 3 4

#global variation
def func(x,y):
    global a
    a=45
    x,y=y,x
    b=33
    b=17
    print(a,b,x,y)
a,b,x,y=3,15,3,4
func(9,81)
print(a,b,x,y)
#45 17 81 9
#45 15 3 4

