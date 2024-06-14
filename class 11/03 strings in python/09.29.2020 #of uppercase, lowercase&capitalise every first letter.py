#Program to find number of uppercas letter, lowercases letters, alphabets, numbers
line=input('enter a line')
lowercount=uppercount=0#number of upper and lowercase
digicount=alphacount=0#number of digits and alphabets
for a in line:
    if a.islower():
        lowercount+=1
    elif a.isupper():
        uppercount+=1
    elif a.isdigit():
        digicount+=1
    elif a.isalpha():
        alphacount+=1
#in the above block, all for can be if statements, or a combination of elif,else,etc.
print('number of lowercase characters:',lowercount)
print('number of uppercase characters:',uppercount)
print('number of digits is:',digicount)
print('number of alphabets is:',alphacount)

#capitalising every 1st letter
str1=input('enter a string')
print('original string',str1)
str2=' '
x=str1.split()#breaks up the string
for a in x:
    str2=a.capitalize()+' '#concatination along with capitalize method
print(str2)
