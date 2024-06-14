#changes that occur in the list-mutable property
#traversing a list-use looping conditions
#lists also follow similar props as strings
list1=['l','e','a','r','n','p','y','t','h','o','n']
for i in list1:
    print(i)

list=['p','y','t','h','o','n']
n=len(list) #counts the total number of characters in the string
for i in range(n):
    print(list[i])
print('the total number of characters are;',n) #n=6

#python allows us to compare lists in lexicographical order. Each element is induvidually compared alphabetical or dictionary order
L1,L2=[10,20,30],[10,20,30]
L3=[10,[20,30]]
L1==L2
print(L1==L2)#true
print(L2==L3)#false
L4=[10,[20,30]]
L3==L4#true

L1=[20,30]
L2=[20,30]
L3=['20','30']
L4=[20.0,30.0]
L5=[20,30,40]
print(L1==L2) #True
print(L1>L2)#False
print(L4>L1)#False
print(L4==L1)#True

#operations on lists
#concatenation-combining of strings
list1=['red','green']
list2=[10,20,30]
list1=list1+['blue']
print(list1)
list=['learn','python']+['programing']
print(list)
