#the .lstrip function-removing characters from the left
str='         green revolution'
print(str.lstrip())
                        #output
                        #green revolution
str='green'
print(str.lstrip('rg')) #you can remove letters too
                        #output
                        #een

print(str.lstrip('e'))  #you cannot remove random letters, only leftmost
                        #output
                        #green
str='een'
print(str.lstrip('e'))  #it removes repetitive letters too!
                        #output
                        #n

#the .rstrip() function-removing characters from the right
str='hello world'
print(str.rstrip('world'))
                        #output
                        #hello

str='priyadharshini sridhar'
x=str.rstrip('dhar')    #combined usage of .lstrip and.rstrip
y=x.lstrip('pri')
print(y)

#.isspace function-checking if a string is just a blank space
str=' '
print(str.isspace())    #output
                        #True

str=''                  #only quotes, no space given
print(str.isspace())    #output
                        #False
str='py'
print(str.isspace())    #output
                        #False

#istitle() function-checking if the first letter of each word is capital
str1='All Learn Python'
print(str1.istitle())   #output
                        #True
str1='aLl LeArN pyThON'
print(str1.istitle())   #output
                        #False

#.join function
a='abcd'
b='#'
b.join(a)               #output
                        #'a#b#c#d'
b='!@#$'
b.join(a)               #output
                        #'a!@#$b!@#$c!@#$d'

a.join(b)               #output
                        #'!abcd@abcd#abcd$'

