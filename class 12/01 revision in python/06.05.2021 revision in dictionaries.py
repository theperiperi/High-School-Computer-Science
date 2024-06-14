#revision of dictionaries
#write a python program to add a key to a dictionary
d = {0:10, 1:20}
print(d)                #{0: 10, 1: 20}
d.update({2:30})
print(d)                #{0: 10, 1: 20, 2: 30}

#contacatination of dictionaries
#method1
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
dic1.update(dic2)
dic1.update(dic3)
print(dic1)             #{1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

#method2
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
dic4 = {}
for d in (dic1, dic2, dic3):
    dic4.update(d)
print(dic4)             #{1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}            

#write a program to iterate over dictionaries using for loops
#means that we have to identify keys and values
d = {'x': 10, 'y': 20, 'z': 30} 
for dict_key, dict_value in d.items():
    print(dict_key,'->',dict_value)
    #x -> 10
    #y -> 20
    #z -> 30

#write a python program to merge two dictionaries
d1 = {'a': 100, 'b': 200}
d2 = {'x': 300, 'y': 200}
d = d1.copy()          #copies value to another dictionary(doesnt erase original value)
d.update(d2)
print(d)                #{'a': 100, 'b': 200, 'x': 300, 'y': 200}

#write a python program to sum all the items in the dictionary
d={1:100,2:200,3:300}
v=d.values()            #takes values
s=sum(v)                #sum of values
print(s)                #600

#combining previous solution line 2 and 3 for efficiancy
d={1:100,2:200,3:300}
s=sum(d.values())                
print(s)                #600










