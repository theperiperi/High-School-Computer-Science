#using if else condition (odd and even example)
a=int(input("enter the number"))
if(a%2==0):
    print("it is an even number")
else:
    print ('it is an odd number')

x=int(input("enter the value of first number"))
y=int(input("enter the value of second number"))
remainder=x%y
if(remainder==0):
    print(x,"is divisible by",y)
else:
    print(x,"is not divisible by",y)
    
