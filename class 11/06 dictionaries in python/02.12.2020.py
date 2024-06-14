#number of characters
str=input('enter the string')
dict1={}
for ch in str:
    if ch in dict1:
        dict1[ch]+=1
    else:
        dict1[ch]=1
for key in dict1:
    print(key,':',dict1[key])

#write a program to store students info like admission, rollno, name, marks
