#extend method=list1.extend(list2)
list1=[5,4,7,8]
list2=[12,13,15]
list1.extend(list2)
print(list1)

# vowel list
vowel = ['a', 'e', 'i', 'u']
# 'o' is inserted at index 3
# the position of 'o' will be 4th
vowel.insert(3, 'o')
print('Updated List:', vowel)#aeiou

#reverse()
list1=[24,56,44,34,36]
list1.reverse()
print(list1)

#replacing an element as per index in a list
list=[1,2,3]
list[2]=4
print(list)
#[1,2,4]

#making a sublist
l1=[10,20,30,40,50]
l2=l1[-1:-4]
print(l2)
#[]

l1=[10,20,30,40,50]
l2=l1[1:4]
print(l2)
#20,30,40

#string is considered as single element
l1=[5,'book',4,3,'new']
print(len(l1))

#ordering lists
l1=[10,4,20,98,2,100]
l1.sort()
print(l1)
#2,4,10,20,98,100-ascending

l1=['green','blue','red','purple','yellow']
l1.sort()
print(l1)
#alphabetical
['blue', 'green', 'purple', 'red', 'yellow']











