#*string length function*
str1='this is Aashish\'s pen'
print(len(str1))        #slash not counted as character
                        #output=21

#*capitalise function*
str1='welcome'
print(str1.capitalize())
                #output
                #'Welcome'

#*split function*
x='bluered;green'
print(x.split(':'))     #['bluered;green']
print(x.split(';'))     #['bluered', 'green']
print(x.split())        #['bluered;green']
y='hello welcome to python'
print(y.split())        #['hello', 'welcome', 'to', 'python']
z='123;12322;123221;'
print(z.split())        #['123;12322;123221;']
print(z.split('1'))     #['', '23;', '2322;', '2322', ';']

#*replace function*
string='this is a string example'
print(string.replace('is','was'))
                #output
                #thwas was a string example
                #note that th'is' changes to th'was'
string='cold coffee'
print(string.replace('cold','hot'))
                #output
                #hot coffee

#*find method*
word='green revolution'
result=word.find('green')
print(result)
                #output
                #0
result=word.find('Green')
print(result)
                #output
                #-1

#*isalpha function* is it a letter?
string='hello world'
print(string.isalpha())
                #output
                #False
string='helloworld'
print(string.isalpha())
                #output
                #True
string='hElLoAlpHa'
print(string.isalpha())
                #output
                #True

#*isdigit function* is it a number?
string='123'
print(string.isdigit())
                #output
                #True

#*lower function* making text lowercase
str='LEARNING PYTHON'
print(str.lower())
                #learning python

#*upper function* making text uppercase
str='learning python'
print(str.upper())
                #output
                #LEARNING PYTHON

#*isupper* *islower* checking if text is uppercase or lowercase
x='learning python'
print(x.isupper())
                #output
                #False
print(x.islower())
                #output
                #True




