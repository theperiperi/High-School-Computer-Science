#contcantination of tuples
t1=input('enter the first tuple')
t2=input('enter the second tuple')
t=t1+t2
x=tuple(t)
print(x)


fib=[]
a,b=0,1
for i in range(0,12,1):
    a,b=b,a+b
    fib.append(a)
a=tuple(fib)
print(fib)

