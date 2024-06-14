#write a program to perform all the string operations as a menu driven program

#write a program to count the number of each vowel in a string
str=input('enter the string')
a=0
e=0
i=0
o=0
u=o
for char in str:
    if char=='a':
        a+=1
print(a)
for char in str:
    if char=='e':
        e+=1
print(e)
for char in str:
    if char=='i':
        i+=1
print(i)
for char in str:
    if char=='o':
        o+=1
print(o)
for char in str:
    if char=='u':
        u+=1
print(u)

#Write a program that takes a sentence as an input from the user where each
#word in the sentence is seperated by a space and replaces each blank with a
#hyphen and then prints the modified sentence
str=input('enter a sentence')
print(str.replace(' ','-'))

#write a program to accept an integer list and search a particular value
#in the list, if it exists then output should display exists, otherwise print
#does not exist
list=input('enter the list')
val=input('enter the value to be searched')
if val in list:
    print('exists')
else:
    print('does not exist')
    

#write a program to add 5 to all the odd values, and 10 to all the even values
#of the list, and finally displays the list
list=input('user please give the list:')
for element in list:
    if element%2==0:
        element+=10
        print(element)
    else:
        element+=5
        print(element)














