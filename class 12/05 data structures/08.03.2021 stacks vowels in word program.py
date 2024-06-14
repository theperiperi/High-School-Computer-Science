vowels=['a','e','i','o','u']
word=input('enter a word to search for vowels')
stack=[]
count=0
for letter in word:
    if letter in vowels:
        count+=1
        if letter not in stack:
            stack.append(letter)
print(stack)
print('the number of vowels',len(stack))
print('number of vowels',count)
      
