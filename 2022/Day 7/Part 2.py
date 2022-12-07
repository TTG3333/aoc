with open("Input.txt", "tr") as F:
    lines = F.read().splitlines()

currentPos = []
tree = {}
listing = False
for line in lines:
    if line.startswith("$ cd"):
        listing = False
        pos = line[5:]
        if pos == "/":
            currentPos = ["/"]
            if "/" not in tree:
                tree["/"] = {"value": 0, "dirs": [], "recursion": False}
        elif pos == "..":
            currentPos.pop()
        else:
            currentPos.append(pos)
            path = "/" + "/".join(currentPos[1:])
            if path not in tree:
                tree[path] = {"value": 0, "dirs": [], "recursion": False}
    elif line.startswith("$ ls"):
        listing = True
    elif line.startswith("dir"):
        path = "/" + "/".join(currentPos[1:])
        tree[path]["dirs"].append(line[4:])
    else:
        path = "/" + "/".join(currentPos[1:])
        tree[path]["value"] += int(line.split(" ")[0])

def computeTotalValue(di, tree, path = ""):
    newPath = path + "/" + di if path != "/" else "/" + di
    if tree[newPath]["recursion"]:
        return
    for d in tree[newPath]["dirs"]:
        computeTotalValue(d, tree, newPath)
        newPath2 = newPath + "/" + d if newPath != "/" else "/" + d
        tree[newPath]["value"] += tree[newPath2]["value"]
    tree[newPath]["recursion"] = True

def sum2(vals, key = lambda a: a):
    s = 0
    for v in vals:
        s += key(v)
    return s

computeTotalValue("", tree)
spaceToFree = 30000000 - 70000000 + tree["/"]["value"]
print(min(tree.values(), key = lambda a: a["value"] if a["value"] > spaceToFree else float("inf"))["value"])