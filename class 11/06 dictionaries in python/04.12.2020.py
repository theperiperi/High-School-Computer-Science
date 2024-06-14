#removing an item from dictionary (using delete command)
a={'mon':'monday','tues':'tuesday','wed':'wednesday'}
del a['wed']
print(a)
#{'mon': 'monday', 'tues': 'tuesday'}

#pop method
print(a.pop('tues'))
#tuesday
print(a)
#{'mon': 'monday'}

#membership operators
a={'mon':'monday','tues':'tuesday','wed':'wednesday'}
print(a)
print('wed' in a)
#true
print('fri' in a)
#false
print('fri' not in a)
#true

#length function
print(len(a))
#3

#clear method
print(a.clear())
#none

#append method
a={'mon':'monday','tues':'tuesday','wed':'wednesday'}
a['thu']='thursaday'
print(a)


