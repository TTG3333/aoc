import json

with open("Input.txt", "tr") as F:
    data = json.load(F)

def explore(dat):
    total = 0
    if isinstance(dat, list):
        for item in dat:
            if isinstance(item, int):
                total += item
            elif isinstance(item, (list, dict)):
                total += explore(item)
    elif isinstance(dat, dict):
        if "red" in dat.values():
            return 0
        for item in dat.values():
            if isinstance(item, int):
                total += item
            elif isinstance(item, (list, dict)):
                total += explore(item)
    return total

print(explore(data))