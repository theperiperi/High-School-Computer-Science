#length of string
string=input('enter the string')
string=len(string)
print('the length of the string is',string)

#write a program to concatinate two strings
str1=input('enter string#1')
str2=input('enter string#2')
str=str1+str2
print(str,'is the concatinated string')

#write a program to copy string from source to destination
str1=input('enter the string')
str2=str1
print(str2)

#write a python program to determine the length of the string without using string length
string=input('enter the string')
count=0
for i in string:
    count+=1
print(count,'is the length of the string')

# Python program to check if a string is palindrome or not
x = input('enter the word to check')
w = ""
for i in x:
    w = i + w
if (x == w):
    print("Yes")
else:
    print("No")
