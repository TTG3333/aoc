import json

with open("Input.txt", "tr") as F:
    packets = [json.loads(x) for x in F.read().splitlines() if x != ""]
packets.append([[6]])
packets.append([[2]])

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

def order(p): # QuickSort
    if len(p) < 2:
        return p
    elif len(p) == 2:
        if compare(*p):
            return p
        else:
            return p[::-1]
    else:
        pivotIndex = len(p)//2
        smaller = order([v for v in p if compare(v, p[pivotIndex]) == True])
        middle = [v for v in p if compare(v, p[pivotIndex]) == None]
        greater = order([v for v in p if compare(v, p[pivotIndex]) == False])
        p = smaller + middle + greater
        return p

packets = order(packets)
print((packets.index([[2]])+1) * (packets.index([[6]])+1))