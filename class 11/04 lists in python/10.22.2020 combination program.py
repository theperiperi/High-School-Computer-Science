#menu driven program
list1=[22,4,16,38,13]
choice=0
while True:
    print('the list has the following elements',list1)
    print('\n list operations\n')
    print('1. append an element')
    print('2. insert an element in the desired position')
    print('3. append a list to the given lists')
    print('4. modify existing element')
    print('5. delete an existing element by its position')
    print('6. deleting an existing element by its value')
    print('7. sort the list in ascending element')
    print('8. sort the list in descending order')
    print('9.sidplay the list')
    print('10.exit')
    choice=int(input('enter your choice(1 to 10)'))
    #append element
    if choice==1:
        element=int(input('enter the element to be appended:'))
        list1.append(element)
        print('the element to be appended\n')
    #insert element in desired position
    elif choice==2:
        element=int(input('enter the element to be inserted'))
        pos=int(input('enter the position'))
        list1.insert(pos,element)
        print('the element has be inserted')
    #append a list to the given limit
    elif choice==3:
        newlist=int(input('enter the list to be appended;'))
        list1.extend(newlist)
        print('the list has been appended\n')
    #modify an existing element
    elif choic==4:
        i=int(input('enter the position of the element to be modified:'))
        if i<len(list1):
            newelement=int(input('enter a new element;'))
            oldelement=list1[i]
            list1[i]=newelement
            print('the element',oldelement, 'has been modified /n')
        else:
            print('position of the element is more than the length of the list')
    #delete an existing element by position
    elif choice==5:
        i=int(input('enter the position of the element to be deleted'))
        if i<len(list1):
            element=list.pop(i)
            print('the element',element,'has been deleted/n')
        else:
            print('\n position of the element is more than the length of the list')
    #delete an existing element by value
    elif choice==6:
        element=int(input('\nenter the element to be deleted'))
        if element in list1:
            list1.remove(element)
            print('the element',element,'has been deleted')
        else:
            print('\nelement', element, 'is not present in the list')
    #sorting the list in ascending order
    elif choice==7:
        list1.sort()
        print('the list has been sorted')
    #sorting the list in descending order
    elif choice==8:
        list1.sort(reverse==True)
        print('\n the list has been sorted in reverse order')
    #displaying the list
    elif choice==9:
        print('the list is',list1)
    #exit
    elif choice==10:
        break
    else:
        print('choice is not valid')





















            
        
