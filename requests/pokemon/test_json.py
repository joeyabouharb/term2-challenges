import json

class Nothing:
    def __init__(self, items: dict):
        for key in items.keys():
            setattr(self, key, items[key])

nothing_dict = {
    "item1" : 312,
    "item2" : {
        "trash": 21
    }
}
with open('test.json', 'w+') as file:
    json.dump(nothing_dict, file, indent=2)

with open('test.json', 'r') as file:
    nothing_dict = json.load(file)
nothing = Nothing(nothing_dict)

print(nothing.item2)