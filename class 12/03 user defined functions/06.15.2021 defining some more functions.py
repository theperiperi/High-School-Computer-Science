#function to multiply 2 numbers
x=int(input('enter x'))
y=int(input('enter y'))
def mult(x,y):
    print(x*y)
mult(x,y)

#pascals triangle program
def pastri(n):
    trow=[1]
    y=[0]
    for x in range(max(n,0)):
        print(trow)
        trow=[1+r for l,r in zip(trow+y,y+trow)]
    return n>=1
n=int(input('enter n value')) #5
pastri(n)
#[1]
#[1, 2]
#[1, 2, 3]
#[1, 2, 3, 4]
#[1, 2, 3, 4, 5]

#subtracting 2 numbers
def sub(x,y):
    print(x-y)
x=int(input('enter x'))
y=int(input('enter y'))
sub(x,y)

#getting the remainder
def rem(x,y):
    print(x%y)
x=int(input('enter x'))
y=int(input('enter y'))
rem(x,y)

#understanding zip method
a=('hello','welcome','to','class12')
b=('all','to','csc')
x=zip(a,b)
print(tuple(x))

#understanding zip
num_list=[1,3,5]
str_list=['one','three','five']
#no iterables
result=zip()
#converting iterators into list
res_list=list(result)
print(res_list)
#two iterables
result=zip(num_list,str_list)
print(result)
#set method
res_set=set(result)
print(res_set)









