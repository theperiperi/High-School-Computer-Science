list1=[4,3,6,5,7,8,0]
for i in range(1,len(list1)):
    value=list1[i]
    #move elements of list[0..i-1], that are
    #greater than value, to one position ahead
    #of their current position
    j=i-1
    while j>=0 and value<list1[j]:
        list1[j+1]=list1[j]
        j-=1
    list1[j+1]=value
print(list1)
#[0, 3, 4, 5, 6, 7, 8]
