#a function is defined using def keyword in python
def myfunction():
#function definition
    print('sample function created')
#no output here
myfunction()#function call
#only if a function call is present, output will be printed

#defining a function for even or odd
def evenodd(x):
#(x) is called passing an argument
    if(x%2==0):
        print('even')
    else:
        print('odd')
#driver code aka function call
evenodd(2)#even
evenodd(3)#odd
#getting the argument from the user
x=int(input('enter x'))
evenodd(x)

#defining a function for multiple of 10
def x10(x):
    if x%10==0:
        print('yes')
    else:
        print('nope')
x=int(input('enter x'))
x10(x)

#function for alpha?
def alphaorno(x):
    if x.isalpha()==True:
        print('yes')
    else:
        print('No')
x=input('enter x')
alphaorno(x)

#function for addition
def add(x,y):
    print(x+y)
a=int(input('enter a'))
b=int(input('enter b'))
add(a,b)

#actual parameters:
#parameters that are specified in the function call
#actual parameters are passed by calling functions
#in above program (a,b) are actual

#formal parameters:
#specified in the function definition
#formal parameters are passed by the called functions
#in above program (x,y) are formal































