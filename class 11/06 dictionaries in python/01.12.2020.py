#making a simple table
d={1:'one',2:'two',3:'three',4:'four'}
for i in d:
    print(i,':',d[i])
#1 : one
#2 : two
#3 : three
#4 : four

#table of classes and streams
classxi=dict()
n=int(input('enter the number of sections in class xi:'))
i=1
while i<=n:
    a=input('enter section')
    b=input('enter stream name')
    classxi[a]=b
    i+=1
print('class','\t','section','\t','stream name')
for i in classxi:
    print('xi','\t',i,'\t',classxi[i])

#class 	 section 	 stream name
#xi 	 a 	 math
#xi 	 b 	 eng
#xi 	 c 	 sci
#xi 	 d 	 bio
#xi 	 e 	 chem

#len method
d1={1:10,2:30,3:30,4:50,5:60}
print(len(d1))
#5 (number of pairs)

#clear method
d1={1:10,2:30,3:30,4:50,5:60}
d1.clear()
print(d1)
#{}

#get method
d1={'sun':'sunday','mon':'monday','tues':'tuesday'}
print(d1.get('mon'))
#monday

#items method
d1={'sun':'sunday','mon':'monday','tues':'tuesday'}
print(d1.items())
#dict_items([('sun', 'sunday'), ('mon', 'monday'), ('tues', 'tuesday')])

#sun, mon, tues : keys
#sunday, monday, tuesday : values

#values and keys method
d1={'sun':'sunday','mon':'monday','tues':'tuesday'}
print(d1.values())
d1={'sun':'sunday','mon':'monday','tues':'tuesday'}
print(d1.keys())
#dict_values(['sunday', 'monday', 'tuesday'])
#dict_keys(['sun', 'mon', 'tues'])

#write a program to store the name of employees and their salaries in a dictionary

#write a program to count the number of times a character appears in a given string
#using a dictionary














