import json, pickle

my_favourite_group = {
'name': 'Г.М.О.',
'tracks': ['Последний месяц осени', 'Шапито'],
'Albums': [{'name': 'Делать панк-рок','year': 2016},
{'name': 'Шапито','year': 2014}]
}

a = json.dumps(my_favourite_group)
b = pickle.dumps(my_favourite_group)
print(a)
print(type(a))
print(b)
print(type(b))

with open("group.pickle", "wb") as f:
    pickle.dump(my_favourite_group, f)
    

with open("group.json", "w", encoding= "utf-8") as f:
    json.dump(my_favourite_group, f)