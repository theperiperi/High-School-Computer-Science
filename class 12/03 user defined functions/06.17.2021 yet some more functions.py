#defining greatest integer
x=int(input('enter x'))
y=int(input('enter x'))
def greater(x,y):
    z=max(x,y)
    print(z)
greater(x,y)

#defining factorial function
lim=int(input('enter limit'))
x=1
def fact(lim):
    if lim==0:
        print(1)
    if lim<0:
        print('undefined')
    if lim>0:
        x=1
        y=1
        while x in range(1,lim+1):
            y=y*x
            x+=1
    print(y)

fact(lim)

#defining function for sum of n natural numbers
lim=int(input('enter limit'))
def sumnat(lim):
    y=0
    x=0
    while x in range(0,lim+1):
        y=y+x
        x+=1
    print(y)

sumnat(lim)
    




































