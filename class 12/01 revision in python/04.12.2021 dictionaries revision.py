#making a dictionarythisdict = {"brand": "Ford","model": "Mustang","year": 1964}print(thisdict)#{'brand': 'Ford', 'model': 'Mustang', 'year': 1964}print(thisdict["brand"])#getting value by giving input as key#Ford#dictionaries cannot have two items with the same key#here the key ('year') is overwrittenthisdict = {"brand": "Ford","model": "Mustang","year": 1964,"year": 2020}print(thisdict)#{'brand': 'Ford', 'model': 'Mustang', 'year': 2020}print(len(thisdict))#3print(thisdict['year'])#2020#for assigning multiple strings as valuesthisdict = {  "brand": "Ford",  "electric": False,  "year": 1964,  "colors": ["red", "white", "blue"]}print(thisdict)#{'brand': 'Ford', 'electric': False, 'year': 1964, 'colors': ['red', 'white', 'blue']}print(type(thisdict))#<class 'dict'>#get methodthisdict = {"brand": "Ford","model": "Mustang","year": 1964}x = thisdict["model"]print(x)#Mustangx = thisdict.get("model")print(x)#Mustangx = thisdict.keys()print(x)#dict_keys(['brand', 'model', 'year'])#focusing on keyscar = {"brand": "Ford","model": "Mustang","year": 1964}x = car.keys()print(x) #before the change#dict_keys(['brand', 'model', 'year'])car["color"] = "white"print(x) #after the change#dict_keys(['brand', 'model', 'year', 'color'])#focusing on valuesx = thisdict.values()car = {"brand": "Ford","model": "Mustang","year": 1964}x = car.values()print(x) #before the change#dict_values(['Ford', 'Mustang', 1964])car["year"] = 2020print(x) #after the change#dict_values(['Ford', 'Mustang', 2020])#membership in dictionariesthisdict = {  "brand": "Ford",  "model": "Mustang",  "year": 1964}if "model" in thisdict:  print("Yes, 'model' is one of the keys in the thisdict dictionary")#Yes, 'model' is one of the keys in the thisdict dictionarythisdict = {"brand": "Ford","model":"Mustang","year": 1964}thisdict["year"] = 2018