#using eval:getting input as list
x=eval(input('enter the list'))
for i in x:
    if i%2==0:
        print(i)

#program for linear search-traversing a complete list for searching for a single element
list1=eval(input('enter the list elements'))
length=len(list1)
element=int(input('enter the element to be searched for'))
for i in range(0,length):
    if element==list1[i]:
        print('the element is found in index:',i)
        break
else:
    print('element not in list')

#showing the difference between eval and no eval output
x=1
print('x+1')#concatination output
x=1
print(eval('x+1'))#integer output

#write a program to exchange the first half elements
#of the list with second half elements
#assuming the list  hass even number of elements
list1=eval(input('enter the list'))#[1,2,3,4]
x=int(len(list1)/2)
for i in range(x):
    list1[i],list1[x+i]=list1[x+i],list1[i]
print(list1)#[3,4,1,2]
