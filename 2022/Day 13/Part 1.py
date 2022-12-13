import json

with open("Input.txt", "tr") as F:
    lines = F.read().splitlines()

def compare(elem1, elem2): # Returns None if they're equal, true if elem1 < elem2
    if elem1 == elem2:
        return None
    if isinstance(elem1, int) and isinstance(elem2, int):
        return elem1 < elem2
    elif isinstance(elem1, int):
        elem1 = [elem1]
    elif isinstance(elem2, int):
        elem2 = [elem2]
    for i in range(min(len(elem1), len(elem2))):
        c = compare(elem1[i], elem2[i])
        if c == None:
            continue
        return c
    return None if len(elem1) == len(elem2) else len(elem1) < len(elem2)

count = 0
for i in range(0, len(lines), 3):
    first, second = [json.loads(x) for x in lines[i:i+2]]
    if compare(first, second):
        count += i//3+1
print(count)