import os
cwd=os.getcwd()
print(cwd)
#C:\Users\Akila\Desktop\csc\class 12\file handling

import sys
f1=open('06.30.2021 test3.txt','r')
line1=f1.readline()
line2=f1.readline()
line3=f1.readline()
sys.stdout.write(line1)
sys.stdout.write(line2)
sys.stdout.write(line3)
f1.close()
#prints first three lines

#sys.path
#sys.maximise
#sys.exit

#from here onwards error
s=input('enter the sentence')
def capital():
    i=s[0]
    s[0]=i.capitalise()
    print(s)
capital()

s=input('enter the sentence')
def capital():
    f1=open('testreport.txt','r')
    f2=open(
    
line=line.strip()
linelen=len(line)
str=' '#concatinate
str=str+line[0].upper()
i=1
#loop for uppercase conversion
while i<linelen:
    if line[i]=='.'
    str=str+line[i]
    i=i+1
    if i>=linelen:
        break
    str=str+line[i].upper()
    i=i+1
    if i>linelen
