#converting ND MODIFYING TUPLES

thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)
print(thistuple)
#('apple', 'banana', 'cherry', 'orange')

thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)
print(thistuple)
#('banana', 'cherry')

thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)
print(thistuple)
#('banana', 'cherry')

x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)
#('apple', 'kiwi', 'cherry')

fruits = ("apple", "banana", "cherry")
print(fruits)
#('apple', 'banana', 'cherry')


fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits
print(green)#apple
print(yellow)#banana
print(red)#cherry
