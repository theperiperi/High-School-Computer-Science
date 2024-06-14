#program to find lowest and second lowest number from the 10 numbers input
small=smaller=0
for i in range(10):
    n=int(input('enter the number:'))
    if i==0: #first number is read
        small==n
    elif i==1:#second number is read
        if n<=small:
            smaller=small
            small=n

        else:
            if n<smaller:
                small=smaller
                smaller=n
            elif n<small:
                small=n
print('the lowest number is',small)
print('the second smallest number is',smaller)
#maam is still checking the program


#factorial calculation
num=int(input('hello user,enter a number'))
for i in range(1,num):
    num*=i
print(num)

#generating divisors of a number(factors)
n=int(input('enter an integer'))
for i in range(1,n):
    if n%i==0:
        print(i,'is a divisor of',n)
print('thank you')


    


