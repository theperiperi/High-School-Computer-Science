#the last line of every program is just a line break

print('COMPUTER SCIENCE OFFLINE ASSIGNMENT')
#1.write a program to covert km to m
a=float(input('enter the value in kilometers:'))
b=a*1000
print('the value in meters is:',b,'m')
print('-------------------------------------')

#2.write a program to find the sum of three numbers
a=int(input('enter the 1st number:'))
b=int(input('enter the 2nd number:'))
c=int(input('enter the 3rd number:'))
sum=a+b+c
print ('the sum od the numbers is',sum)
print('-------------------------------------')

#3.write a program to find the volume and surface area of a sphere
r=float(input('enter the radius'))
v=4/3*3.14*r*r*r
print('the volume of the sphere is',v)
s=4*3.14*r*r
print('the surface area of the sphere is',s)
print('-------------------------------------')

#4.program for volume of a cube and area of a square
s=float(input('enter the length of side'))
v=s*s*s
print('volume of a cube=',v)
a=s*s
print('area of a square=',a)
print('-------------------------------------')

#5.find the output
a=4.5
b=2
print (a//b)
#output will show quotient in float,here 2.0)
print('-------------------------------------')

#6.simple operations
a=int(input("enter the value of a"))
b=int(input("enter the value of b"))
c=a+b
d=a*b
e=a/b
f=a-b
print('sum is',c)
print('difference is',f)
print('product is',d)
print('quotient is',e)
print('-------------------------------------')

#7.converting farenheit to celcius
a=int(input('enter the celcius value'))
b=9/5*a
c=32+b
print ('in farenheit it is:',c)
print('-------------------------------------')

#8.find x and y
x=int(input("enter the value of x"))
y=int(input("enter the value of y"))
x=x+y
y=x-y
x=x-y
print('x=',x)
print('y=',y)
#it interchanges the values of x and y, that is,x=y and y=x
print('-------------------------------------')

#9.finding the area and circumference of a circle
r=float(input('enter the radius'))
a=3.14*r**2
c=2*3.14*r
print('the area is',a)
print('the circumference is',c)
print('-------------------------------------')

#10.converting feet into inches
f=float(input('enter the value in feet'))
i=f*12
print('it is equal to',i,'inches')
print('-------------------------------------')

