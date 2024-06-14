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
