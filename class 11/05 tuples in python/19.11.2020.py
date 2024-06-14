tuplex=(2,4,3,5,4,6,7,8,6,1)
s=tuplex[3:5]
#working with tuples and ranges

print(s)
#(5,4)
s=tuplex[:6]
print(s)
#(2,4,3,5,4,6)
s=tuplex[0:]
print(s)
#(2,4,3,5,6,7,8,6,1)
s=tuplex[:]
print(s)
#(2,4,3,5,6,7,8,6,1)

tuplex=tuple('Hello World')
print(tuplex)
#('H', 'e', 'l', 'l', 'o', ' ', 'W', 'o', 'r', 'l', 'd')
s=tuplex[2:9:2]
print(s)
#('l', 'o', 'W', 'r')
s=tuplex[::4]
print(s)
#('H', 'o', 'r')
s=tuplex[9:2:-4]
print(s)
#('l', ' ')
s=tuplex[-2:-10:3]
print(s)
#()

my_tuple=('a','b','c','d')
print(my_tuple[1:])
#('b', 'c', 'd')
print(my_tuple[:2])
#('a', 'b')
print(my_tuple[1:3])
#('b', 'c')
print(my_tuple[::2])
#('a', 'c')



