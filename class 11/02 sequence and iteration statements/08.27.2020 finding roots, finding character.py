#program to calculate and print roots of a quadratic equation a^2+bx+c=0(a!=0)
import math
a=int(input('enter the value of a:'))
b=int(input('enter the value of b:'))
c=int(input('enter the value of c:'))
if(a==0):
    print('the value of a should not be zero')
else:
    delta=b**2-4*a*c
    if(delta>0):
        root1=(-b+math.sqrt(delta))/(2*a)
        root2=(-b-math.sqrt(delta))/(2*a)
        print('roots are real and unequal')
        print('root1=',root1,'root2=',root2)
    elif(delta==0):                                     #you can also use if
        root1=-b/2*a
        print('roots are real and equal')
        print('root1=root2=',root1)
    else:
        print('roots are complex and imaginary')

#finding the character type
ch=input('enter a single character')
if ch>='A' and ch<='Z':
    print('you have entered an uppercase character')
elif ch>='a' and ch<='z':
    print('you have entered a lowercase character')
elif ch>='0' and ch<='9':
    print('you have entered a digit')
else:
    print('you have entered a special character')
    
