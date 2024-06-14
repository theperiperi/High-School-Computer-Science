thisdict = {  "brand": "Ford",  "model": "Mustang",  "year": 1964}
thisdict.update({"year": 2020})
print(thisdict)
#{'brand': 'Ford', 'model': 'Mustang', 'year': 2020}

thisdict = {  "brand": "Ford",  "model": "Mustang",  "year": 1964}
thisdict["color"] = "red"
print(thisdict)
#{'brand': 'Ford', 'model': 'Mustang', 'year': 1964, 'color': 'red'}

thisdict = {  "brand": "Ford",  "model": "Mustang",  "year": 1964}
thisdict.update({"color": "red"})
print(thisdict)
#{'brand': 'Ford', 'model': 'Mustang', 'year': 1964, 'color': 'red'}
