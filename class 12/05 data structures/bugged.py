#write a function in python insert(arr,data),delete(arr,data) for performing
#insertion and deletion operations of a stack. Arr is the list used for
#implementing stack. data is the value to be inserted

arr=eval(input('enter initial list'))
data=input('enter data to be inserted or deleted')
def insert(arr,data):
    arr=arr.append(data)
    return arr
    

def delete(arr,data):
    if len(arr)==0:
        print('underflow')
    else:
        data=int(data)
        arr=arr.pop(data)
    print(arr)

insert(arr,data)
delete(arr,data)
