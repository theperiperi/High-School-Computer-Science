#example 1
file1=open('07.07.2021 test1.txt','r')
vowels=0
consonants=0
uppercase=0
lowercase=0
str1=file1.read()

for i in str1:
    if i>='a' and i<='z':
        lowercase+=1
    elif i>='A' and i<='Z':
        uppercase+=1

for j in str1:
    j=j.lower()
    if j=='a' or j=='e' or j=='i' or j=='o' or j=='u':
        vowels+=1

    else:
        if j.isalpha():
            consonants+=1

print('lowercase count',lowercase)
print('uppercase count',uppercase)
print('vowels count',vowels)
print('consonants count',consonants)

#lowercase count 5
#uppercase count 4
#vowels count 3
#consonants count 6
#for 'hello 123 TEST'


