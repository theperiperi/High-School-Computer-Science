#to print the sums of even and odd natural numbers(limit)
n=int(input('the number limit:'))
c=1
x=y=0 #sum_even=sum_odd=0...im taking simpler variables
while c<=n:
    if c%2==0:
        x+=c #x=x+c
    else:
        y+=c #y=y+c
    c+=1
print('sum of even numbers:',x)
print('sum of odd numbers is:',y)

#using breaks in a loop
a=b=c=0
a=int(input('enter number1:'))
b=int(input('enter number2:'))
while a>0:
    if b==0:
        print('division by zero','aborting')
        break
    else:
        c=a/b
        print('quotient',c)
        break
print('program is over')

#find the logic of the following
for a in range(3):
    for b in range(5,7):
        print("*",end='')
    print()

#part b of prev question
for a in range(3):
    for b in range(5,8):
        print('*',end='')
    print()
    
