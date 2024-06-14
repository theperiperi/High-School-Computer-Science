#ranges in tuples
tp1=(10,12,14,20,22,24,30,32,34)
print(tp1[3:30])#(20, 22, 24, 30, 32, 34)
print(tp1[-15:7])#(10, 12, 14, 20, 22, 24, 30)
print(tp1[0:10:2])#(10, 14, 22, 30, 34)
print(tp1[2:10:3])#(14, 24, 34)
print(tp1[::3])#(10, 20, 30)
print(tp1[2:5]*3)#(14, 20, 22, 14, 20, 22, 14, 20, 22)
print(tp1[2:5]+(3,4))#(14, 20, 22, 3, 4)
print(tp1[-9:7])#(10, 12, 14, 20, 22, 24, 30)

#comparisons and booleans in tuples
a=(2,3)
b=(2,3)
print(a==b)#True
c=('2','3')
print(a==c)#False
print(a>b)#False
d=(2.0,3.0)
print(d>a)#False
print(a>d)#False
e=(2,3,4)
print(a>e)#False
print(e>a)#True


#Write a python program which takes a tuple t and returns the second largest
#element of the tuple t
T=(23,45,34,66,77,70)
maxvalue=max(T)
length=len(T)
secmax=0
for a in range(length):
    if secmax<T[a]<maxvalue:
        secmax=T[a]
print('second largest value is',secmax)
        
