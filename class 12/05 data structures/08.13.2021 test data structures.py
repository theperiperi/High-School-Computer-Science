codes=eval(input('enter list'))
def swapmiddle(codes): 
    x=0 
    midval=len(codes)//2 
    while x<midval: 
        codes[x],codes[midval+x]=codes[midval+x],codes[x] 
        x+=1 
    print(codes)
swapmiddle(codes)

ml= [1,4,9,16,25,36,49,64,81,100]
li=[]
for ele in ml:
    if ele%2==0:
        li.append(ele)
print(li)

v=[1,2,3,4,3,2,1]
def mvisit(v):
    x=max(v)
    print(x)
mvisit(v)

lst=eval(input('enter the list'))
v=input('enter the item to locate')
def find_in_list(lst):
    for ele in range(len(lst)):
        if lst[ele]==v:
            print(lst[ele])
        else:
            print(-1)
find_in_list(lst)

