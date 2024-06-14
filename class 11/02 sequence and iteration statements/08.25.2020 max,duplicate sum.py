#maximum value
x=int(input('enter the value of first number:'))
y=int(input('enter the value of second number:'))
z=int(input('enter the value of third number:'))
max=x
if y>max:
    max=y
if z>max:
    max=z
print('largest number is',max)

#minimum value
x=int(input('enter the value of first number:'))
y=int(input('enter the value of second number:'))
z=int(input('enter the value of third number:'))
min=x
if y<min:
    min=y
if z<min:
    min=z
print('largest number is',min)

#maximum value(float)
x=float(input('enter the value of first number:'))
y=float(input('enter the value of second number:'))
z=float(input('enter the value of third number:'))
max=x
if y>max:
    max=y
if z>max:
    max=z
print('largest number is',max)

#finding sum and duplicate sum
sum1=sum2=0
x=int(input('enter 1st number'))
y=int(input('enter 2nd number'))
z=int(input('enter 3rd number'))
sum1=x+y+z
if x!=y and x!=z:               #!= means not equal to
    sum2+=x
if y!=x and y!=z:
    sum2+=y
if z!=x and z!=y:
    sum2+=z
print('numbers are',x,y,z)
print('sum of three given numbers are',sum1)
print('sum of three non duplicat numbers',sum2)


































































































