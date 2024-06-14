#reads a line and counts substring occurance
s = 'hellohellohello'
sb = 'hello'
results = 0
sub_len = len(sb)
for i in range(len(s)):
    if s[i:i+sub_len] == sb:
        results += 1
print (results)

#write a program to count the number of vowels in the string pineapple
word=input('enter the string') 
count=0
for letter in word:
    if letter in ('a','e','e','o','u'):
        count+=1
print(count)

#write a program that diplays the longest substring of a given string
str1=input('enter a string')
word=str1.split()
maxlength=0
maxword=''
for i in word:              #different words in input
    x=len(i)                #length of all the words
    if x>maxlength and i.isalpha()==True:#if word has more letters than current longest string
        print(i)            
        maxword=i           #this is the longest word
print('substring of max length is',maxword)

# Python program to check if a string is palindrome or not

x =input('enter word')
w = ""
for i in x:
    w = i + w
if (x == w):
    print("Yes")
else:
    print("No")




