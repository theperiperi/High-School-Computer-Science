#concatenation operator
'2'+'book'       
                    #'2book'
'hello'+'world'     
                    #'helloworld'
4*'2'              
                    #'2222'

#membership operators(in and not in)-checking if chars are members of string
#in
st1='my'
st2='my book'
st1 in st2          
                    #True
st2 in st1          
                    #False
#not in
'H' not in "Hello"
                    #False
'f' not in 'hello'
                    #True

#comparing words with ASCII concept
#American standard code for information interchange
#0-9:   0-48 9- 57
#A-65,B-66.....Z-90     a-97,b-98...z-122   
st1='mary'
st2='mac'
st1<st2
                    #False
st2>st1
                    #False
st1>st2
                    #True

#string slicing:slicing is used to retrieve a subset of values.
#A slice of a string is called as a substring
#This extracted substring is called a slice
#Chunk of characters can be extracted from a string using slice operator with two indices(plural of index) in square brackets seperated by a colon symbol
alphabet='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
slice=alphabet[6:15:1]
print(alphabet)
print(slice)
                    #ABCDEFGHIJKLMNOPQRSTUVWXYZ
                    #GHIJKLMNO

#slicing using range(lower_limit+1:upper limit)
A='save money'
A[1:3]
                    #'av'
A[:3]
                    #'sav'
A[3:]
                    #'e money'
A[-2]
                    #'e'
