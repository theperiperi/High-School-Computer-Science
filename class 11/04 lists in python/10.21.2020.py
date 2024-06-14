#CLEAR METHOD:removing all elements in a list
l1=[10,20,30,40,50]
l1.clear()
print(l1)#[]

#COUNT METHOD:counting occurances in a list
l1=[1,2,3,4,5,6]
print(l1.count(1))
                    #another example
l1=[10,10,10,20,30,10]
print(l1.count(10))

#POP METHOD:removing one element from a list
l1=[1,2,3,4,5,1,2,3,4,5]
l1.pop(1)           #element in index 1 is removed
print(l1)           #[1,3,4,5,1,2,3,4,5]

#DELETE METHOD:deleting some elements
#specifying indexes
l1=[100,200,300,400,500]
del l1[3]           #element in index 3 removed....400
print(l1)           #[100,200,300,500]

l1=[100,200,300,400,500]
del l1[1:4]
print(l1)           #[100,500]

#REMOVE METHOD:deleting the value by giving input as the element to be removed itself
#no index specifying
l1=[1,2,3,4,5,6,7,8,9,10]
l1.remove(2)        #removes 2 NOT INDEX 2
print(l1)

#INDEX METHOD:finds the index but IGNORES REPETITIONS
list1=[1,2,3,4,1,1,5]
print(list1.index(1))
print(list1.index(5))

#MAX FUNCTION:find max value
l1=[100,200,300,400,500]
print(max(l1))      #500
print(min(l1))      #100

#to delete all negative numbers and odd numbers in a list
list1=[11,-2,22,-3,33,55,44,-50,46,101,77,-100,42]
len1=len(list1)
i=0
while i<len1:
    if(list1[i]<0):
        del list1[i]
        len1-=1
        i-=1
    elif(list1[i]%2!=0):
        del list1[i]
        len1-=1
        i-=1
    i+=1
print('list after deletion',list1) #[22,44,46,42]


