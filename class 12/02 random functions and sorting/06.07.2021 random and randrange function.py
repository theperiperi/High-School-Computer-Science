#randrange() function
#this function generates a random number between the lower limit and upper limit
#(including lower limit and excluding upper limit-just like in ranges)
import random
a=random.randrange(20)
print(a)

#write a program to generate a random number between 7 and 17 (both inclusive)
import random
a=random.randrange(7,18)
print(a)

#write the code, which always generates 0 with randrange()
import random
a=random.randrange(1)       #concept:always by default, the lower limit is 0
print(a)

#random function
#(random.random is a function, but in import.random it is a module)
#syntax=random.random()
#this function generates a random floating point number from 0 to 1, incl 0 excl 1
#random() function does not take argument, ie YOU cannot put stuff in the brackets

#random number betwenn 10 and 15 using random (both incl)
import random
print(int(random.random( )*6+10))
#logic= () can be any value (0,1), ()*6 any value (0,6)
#whereas 10 is constant and is added, so (10,16) is the implied range here

#generating random 3 digit number
import random
print(int(random.random( )*900+100))

