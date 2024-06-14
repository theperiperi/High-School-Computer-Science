si=dict()
i=1
flag=0
n=int(input('enter the number'))
while i<=n:
    adm=input('\nEnter the admission number:')#\n=new line
    nm=input('\nEnter the name:')
    sec=input('\nEnter the class and section:')
    per=input('\nEnter the percetage of student')
    b=(nm,sec,per)
    si[adm]=b
    i+=1
l=si.keys()
for i in l:
    print('\Admno',i,':')
    z=si[i]
    print('name\t','class\t','per\t')
    for j in z:
        print(j,end='\t')
              
