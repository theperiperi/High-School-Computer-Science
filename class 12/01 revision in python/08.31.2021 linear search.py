def linear(list1):
    count=()
    n=int(input('enter a number'))
    for i in range (len(list1)):
        if list1[i]==n:
            count+=1
            print('the value',n,'is found at the',i,'th position',',','frequency is',count)
linear(list)
