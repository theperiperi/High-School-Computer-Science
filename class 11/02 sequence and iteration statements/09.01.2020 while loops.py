#while statement-checks condition at the beginning of the program
a=5
while a>0:
    print('hello',a)
    a=a-3
print('loop over')#end of while loop    

#using while condition to find squares of a series of numbers
n=1
while n<5:
    print('square of',n,'is',n**2)
    n+=1
print('series printed')

#the infinite loop
a=5
while a>0:
    print(a)
print('thank you')

#breaking the infinite loop-by decrementing the values
a=5
while a>0:
    print(a)
    a-=1
print('thank you')

#finding factorials with while loops
num=int(input('enter the number'))
fact=1
a=1
while a<=num:
    fact*=a
    a+=1
print('factorial of',num,'is',fact)
        
