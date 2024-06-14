#exponential function
x=int(input('enter number'))
y=int(input('enter number')) 
def exp(x,y):
    print(x**y)
exp(x,y)

#fibonacci series
lim=int(input('set limit'))
def fib(lim):
    count=0
    a=0
    b=1
    for count in range (0,lim+1):
        a=a+b  
        b=b+a
        print(a)
        print(b)
        count+=1
fib(lim)



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































    
