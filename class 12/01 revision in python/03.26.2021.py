string=input('enter the string')
print(string[0],':',end='')
for ch in range(1,len(string)):
    if string[ch]=='':
        print(sting[ch+1],'.',end='')

#for getting the ASCII value from python
print(ord('a'))
#for getting the letter from the ASCII value
print(chr(65))
