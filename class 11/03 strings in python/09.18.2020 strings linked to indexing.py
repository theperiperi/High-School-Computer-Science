#using+ in string opertaions
print('enter name')
name=input()
print('hello'+name)
# '+'in strings is known as concatination operator
#it just lierally prints the two strings right next to each other

#same program without concatination +
name=input('enter your name')
print('hello',name)

#indexing using for loop
str='Computer Science'
for a in str:               #no need to mention range function compulsarily
    print(a)                #also the space is counted as a character in the indexing

#string traversing using while loop
str='python processing!'
index=0
#len() function is used to get the length of the string
while index<len(str):
    print(str[index],end='\n')
    #always use index in square brackets
    #\n is an escape sequence...it means display on new line
    index+=1

