x=['hindi','english',1998,1990,1234]
print(x)#initialising list      #brackets and commas also printed
x=[]
print(x)#blank list

x=['hindi','english',1998,1990]
print(x[0])#like indexing, prints hindi
print(x[-3])#uses the reverse indexing concept

#lists and for blocks
a=['1','2','3','4','5']
for i in range(0,len(a)):
    print(a[i])

#printing a selected part (like range) of a list
list=['I','N','D','I','A']
print(list[0:3])
print(list[3:])
print(list[:])

#changing values in a list
x=['hindi','english',1997,2000]
print('value available at index 2:',list[2])
list[2:3]=2001,2002#list[2]=2001 for single item update
print('new value available at index 2:',list[2])
print('new value available at index 3:',list[3])
