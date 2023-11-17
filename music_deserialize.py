import pickle, json

with open("group.json", "r", encoding="utf-8") as f:
    my_group = json.load(f)
    print(my_group)
    print(type(my_group))
    
with open("group.pickle", "rb") as f:
    my_group_2 = pickle.load(f)
    print(my_group_2)
    print(type(my_group_2))