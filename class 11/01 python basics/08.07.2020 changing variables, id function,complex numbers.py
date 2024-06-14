#changing the value of variables
x=3
y=4
z=x+y #3+4=7      z=7
z=z+1 #7+1
x=y #x=4
y=5#y=5
print("x is:",x)
print("y is:",y)
print ("z is:",z)

#usage of variables as constants
x=int(input("enter the value of x"))
y=int(input("enter the value of y"))
z=x+y
x=y
x=50
print('x is',x)
print("y is",y)
print('z is',z)

#address of where the value of x is stored
x=5
id(x)

#example of when it will not work with print statement!
x=5
id(x)
print (x) #prints value of x, which is 5

#example of hoe to correctly print id e=with print statement
x=25
print('address of x:', id(x))

#printing multiple identities
x=5
y=6
z=x+y
print("value of x,y,z",x,y,z)
print('address of x:', id(x))
print('address of y:',id(y))
print('address of z:',id(z))

#representing complex numbers in python
x=2+5j
print (x.real,x.imag)
y=4-2j
print (y.real,y.imag)
x=8j
print (x.real,x.imag)
x=2
print (x.real,x.imag)





