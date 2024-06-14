t=1
print(t)#1
t1=tuple('hello')
print(t1)#('h','e','l','l','o')
l=['a','e','i','o','u']
t1=tuple(l)
print(t1)#('a','e','i','o','u')
t1=tuple(input('enter tuple element'))
print(t1)
tuple=eval(input('enter the tuple to be added:'))
print('tuple you have added',tuple)

vowels=('a','e','i','o','u')
print(vowels[0])#a
print(vowels[4])#u
print(vowels[-1])#u
print(vowels[-5])#a
#tuples are similar to lists in many ways like indexing, slicing,and
#accessing induvidual elements, but they are different in the sense that tuples
#are immutable, while lists are not

#While accessing tuple elements if you pass in a negative index, python adds
#the length of the tuple to the index to get elements forward index

#traversing a tuple
t=('p','y','t','h','o','n')
for a in t:
    print(a)

t=('hello','welcome','to','programming')
length=len(t)
for a in range(length):
    print(t[a])

tp1=(1,3,5)
tp2=(5,6,7)
print(tp1+tp2)

tp1=(1,2,3)
print(tp1+(3,))#(1,2,3,3)
print(tp1*3)#(1,2,3,1,2,3,1,2,3)

tp=(1,2,3,4,5,6,7,8,9,10)
set=tp[3:-3]
print(set)
#4,5,6,7
print(tp[::3])#1,4,7,10
