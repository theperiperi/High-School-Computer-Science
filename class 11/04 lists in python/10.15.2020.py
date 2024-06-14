#copying lists
list_1=[1,2,3]
list_2=list_1   #== doesn't work here
print(list_1)#1,2,3
print(list_2)#1,2,3

list_1=[1,2,3,4,5] #another method for copying(empty colon)
list_2=list_1[:]
print(list_2) #1,2,3,4,5

list1=[10,20,30,40,50]
list2=list(list1) #using list method for copying
print(list2)#10,20,30,40,50

import copy    #using copy method
list1=[1,2,3,4,5]
list2=copy.copy(list1)#always give copy of copy
print(list2)#1,2,3,4,5

#append method-adds a single item to the end of the list, it doesn't create a new list, rather it modifies the original list
#a single element can also be a list, the syntax of append method is list.append()
l1=[10,20,30,40,50]
l1.append(55)
print(l1)

l1=[10,20,30,40,50]
l1.append([55,60])#specifying multiple elements as a single one, makes it eleigible for append method
print(l1)

colour=['red','green','blue']
colour.append('white')
print(colour)#'red','green','blue','white'


    
