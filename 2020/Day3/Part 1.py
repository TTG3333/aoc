with open("Input.txt", "tr") as F:
    lines = F.read().splitlines()
pos = {
    "x": -3,
    "y": -1   
}
trees = 0
for x in range(len(lines)):
    pos["x"] += 3
    pos["y"] += 1
    if lines[pos["y"]][pos["x"]%len(lines[pos["y"]])] == "#":
        trees += 1
print(trees)