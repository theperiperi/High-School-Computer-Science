#question 1
#Write a Python program to generate 26 text files named A.txt, B.txt, and so on
#up to Z.txt.

#import string
#alphabet= string.ascii_lowercase
#for letter in alphabet:
#   with open(letter,'w') as file:
#        file.write(letter)

#simpler asnwer:
#alpha = 'THEQUICKBROWNFOXJUMPEDOVERTHELAZYDOG'
#for i in alpha:
#    f = open(i+'.txt','w')
#    f.close()

#higher order aanswer for same program
#Write a Python program to generate 26 text files named A.txt, B.txt, and so on
#up to Z.txt.
import string, os
if not os.path.exists("letters"):
   os.makedirs("letters")
for letter in string.ascii_uppercase:
   with open(letter + ".txt", "w") as f:
       f.writelines(letter)


#question 2    
#Write a Python program to create a file where all letters of English alphabet
#are listed by specified number of letters on each line
import string
def letters_file_line(n):
   with open("words1.txt", "w") as f:
       alphabet = string.ascii_uppercase
       letters = [alphabet[i:i + n] + "\n" for i in range(0, len(alphabet), n)]
       f.writelines(letters)
letters_file_line(3)

#no of words
filename = input('Enter the name of a file: ')

with open(filename) as f:
    text = f.read()
    print(f'There are {len(text.split())} word(s) in the file')

#ma'am's answer
    
#def count_words(filepath):
#   with open(filepath) as f:
#       data = f.read()
#       data.replace(",", " ")
#       return len(data.split(" "))
#print(count_words("words.txt"))


#question 3
#Write a Python program to read a random line from a file
def count_words(filepath):
   with open(filepath) as f:
       data = f.read()
       data.replace(",", " ")
       return len(data.split(" "))
print(count_words("words.txt"))


#question 4
# Write a Python program to combine each line from first file with the
#corresponding line in second file

#with open('abc.txt') as fh1, open('test.txt') as fh2:
#    for line1, line2 in zip(fh1, fh2):
#        # line1 from abc.txt, line2 from test.txtg
#        print(line1+line2)





























