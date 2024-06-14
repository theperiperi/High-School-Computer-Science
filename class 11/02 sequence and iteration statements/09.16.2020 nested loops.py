#nested while loops
i=2
while (i>=0):
    j=2
    while j>=0:
        print(2,end=" ")
        j=j-1
    print()
    i=i-1

#a nested for loop
for i in range(1,4):
    for j in range(1,1+i):
        print(j,end=' ')
    print()
#(1,2)(1,3)(1,4)
#ouput(omits the upper limit)
#1
#1 2
#1 2 3


