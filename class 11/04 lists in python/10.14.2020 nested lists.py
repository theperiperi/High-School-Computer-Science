#nested_lists
L1=[1,2,[6,7,8],4,5]
print(L1[0])#1
print(L1[1])#2
print(L1[2])#1,2,3
print(L1[3])#4
print(L1[4])#5
print(L1[2][0])#6
print(L1[2][1])#7
print(L1[2][2])#8

#concatenation with lists
list2=[10,20,30]
print(list2*2)#10,20,30,10,20,30
list1=[40,50,60]
print(list2+list1)#10,20,30,40,50,60

#membership testing
#in
x='python'
print('o' in x)#true
list1=[10,20,30]
print(40 in list1)#false
#not in
x=['apple','banana','grapes']
print('lichi' not in x)#true

#list indices
list1=['red','green','blue']
list2=[10,20,30,40,50]
print(list1[2])#blue
print(list1[-1])#blue
print(list2[2])#30
print(list2[-3])#30


