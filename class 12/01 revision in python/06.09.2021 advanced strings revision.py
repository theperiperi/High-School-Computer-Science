txt='hello, and welcome to my world'
x=txt.capitalize()
print(x)
#Hello, and welcome to my world

txt='Hello, And Welcome To My World'
x=txt.casefold()
print(x)
#hello, and welcome to my world

txt='encyclopedia'
x=txt.center(20)
print(x)
#    encyclopedia

txt='no sentence can start with becuase'
x=txt.count('becuase')
print(x)
#1

#unicode string
string='python'
#print string
print('the string is:',string) #the string is:python
#default encoding to utf-8
string_utf=string.encode()
#print result
print('the encoded version is:',string_utf)#the encoded version is:b'python'

txt='hello,welcome to my world'
x=txt.endswith('my world',5,11)
print(x)
#False

txt1="my name is {fname}, I'm {age}".format(age=36,fname='john',number=5)
txt2="my name is {0}, I'm {1}".format('john',36)
txt3="my name is {1}, I'm {0}".format("john",36)
print(txt1)
print(txt2)
print(txt3)
#my name is john, I'm 36
#my name is john, I'm 36
#my name is 36, I'm john

txt='computerS'
x=txt.isalpha()
print(x)
#True

a='\u0030' #unicode for 0
b='\u0047' #unicode for G
print(a.isdecimal())#True
print(b.isdecimal())#False

