with open("Input.txt", "tr") as F:
    connections = [x.split("-") for x in F.read().splitlines()]

caves = {}
for x in connections:
    if x[0] not in list(caves.keys()):
        caves[x[0]] = [x[1]]
    else:
        caves[x[0]].append(x[1])
    if x[1] not in list(caves.keys()):
        caves[x[1]] = [x[0]]
    else:
        caves[x[1]].append(x[0])

def checkCave(caves, cave, c):
    count = 0
    for x in caves[cave]:
        if x == "end":
            count += 1
        elif x in c:
            continue
        elif x == x.lower():
            checked = list(c)
            checked.append(x)
            count += checkCave(caves, x, checked)
        else:
            count += checkCave(caves, x, c)
    return count

print(checkCave(caves, "start", ["start"]))