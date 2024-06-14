#bubble sort program

a=[16,19,11,15,12,14]
#repeating loop len(a) (number of elements)number of times
for j in range(len(a)):
    #initially swapped is False
    swapped=False
    i=0
    while i<len(a)-1:
        #comparing the adjacent elements
        if a[i]>a[i+1]:
            #swapping
            a[i],a[i+1]=a[i+1],a[i]
            #changing the value of swapped
            swapped=True
        i+=1
    #if swapped is false then list is sorted
    #we can stop the loop
    if swapped==False:
        break
print(a)
