#given two lists, write a program that prints 'overlapped', if they have atleast,
#one member in common, otherwise print 'seperated'
listA=eval(input('enter list1:'))
listB=eval(input('enter list2:'))
len1=len(listA)
list2=len(listB)
for a in range(len1):
    ele=listA[a]
    if ele in listB:
        print('overlapped')
        break
else:
    print('seperated')

#write a program that inputs a list of numbers and shifts all the zeros to the
#right and all non zero numbers to the left of the list
1st=eval(input('enter list:'))
length=len(1st)
end=length-1
print('original list:',1st)
i=0
while(i<=end):
    ele=1st[i]
    if ele==0:
        for j in range(i,end):
            1st(j)=1st(j+1)
        else:
            1st[end]=0
            end-=1
    if 1st[i]!=0:
        i+=1
print('zero shifted:',1st)

# Python program to find second largest
# number in a list
# list of numbers - length of 
# list should be at least 2
list1 = eval(input('enter the list'))
 
mx=max(list1[0],list1[1]) 
secondmax=min(list1[0],list1[1]) 
n =len(list1)
for i in range(2,n): 
    if list1[i]>mx: 
        secondmax=mx
        mx=list1[i] 
    elif list1[i]>secondmax and mx != list1[i]: 
        secondmax=list1[i]
 
print("Second highest number is : ",str(secondmax))




