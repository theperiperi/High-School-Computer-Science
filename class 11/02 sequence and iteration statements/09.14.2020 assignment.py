#printing all the prime numbers in a particular range
x=int(input('enter lower limit'))
y=int(input('enter upper limit'))
for num in range(x,y+1):
    if num>1:
        for i in range (2,num):
            if (num%i)==0:
                break
        else:
            print(num)

#checking if a number is prime or not
x=int(input('enter the number'))
for num in(2,x+1):
    if x%num==0:
        print('num not prime')
        break
    if x%num!=0:
        print('num is prime')

#checking if a number is an armstronng number
num=int(input('enter a number'))
sum=0
x=num
while x>0:
    digit=x%10
    sum+=digit**3
    x//=10
if num==sum:
    print(num,'is armstrong number')
else:
    print(num,'is not an armstrong number')
    
