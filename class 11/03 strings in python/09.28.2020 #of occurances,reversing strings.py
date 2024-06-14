#program to find the number of occurances of a character in an inputted string
str=input('enter a string')#say the entred string=interactive, thenstr=interactive
ch=input('enter the character to be searched')#\
count=0
for char in str:
    if char==ch:
        count+=1
print('number of times the character',ch,'occurs in the string is',count)

#program to display string in reverse order
#negative indexing concepts+len function(length of function)
str=input('enter the string')
for i in range (-1,-len(str)-1,-1):
    print(str[i],end='')#end=' ' prints output in single line
