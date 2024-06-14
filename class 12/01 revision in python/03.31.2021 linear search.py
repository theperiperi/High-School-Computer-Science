list=[4,2,8,9,3,7]
x=int(input('enter the number'))
found=False
for i in range (len(list)):
    if(list[i]==x):
        found=True
        print('%d found at %dth posstion'%(x,i))
        print(list)
        break

if(found==False):
    print('%d is not in the list'%x)

#output
#enter the number3
#3 found at 4th posstion
#[4, 2, 8, 9, 3, 7]

#enter the number10
#10 is not in the list

