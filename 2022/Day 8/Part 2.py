with open("Input.txt", "tr") as F:
    grid = F.read().splitlines()

fixedGrid = []
for line in grid:
    fixedGrid.append([{"height": int(x),
        "up": {"h": float("inf"), "dist": 0},
        "down": {"h": float("inf"), "dist": 0},
        "left": {"h": float("inf"), "dist": 0},
        "right": {"h": float("inf"), "dist": 0},
        "vis": False} for x in line])
size = len(grid) # We have a square
dirs = {"up": (0, -1), "down": (0, 1), "left": (-1, 0), "right": (1, 0)}

for dir, diff in dirs.items():
    for i in range(size):
        dists = [-1]*10
        for j in range(size):
            if dir  == "down":
                pos = [i, size - j - 1]
            elif dir == "up":
                pos = [i, j]
            elif dir == "right":
                pos = [size - j - 1, i]
            elif dir == "left":
                pos = [j, i]
            tree = fixedGrid[pos[1]][pos[0]]
            for k in range(10):
                dists[k] += 1
            if j == 0:
                tree[dir]["h"] = tree["height"]
                tree[dir]["dist"] = 0
                tree["vis"] = True
                for k in range(tree["height"]+1):
                    dists[k] = 0
                continue
            otherTree = fixedGrid[pos[1] + diff[1]][pos[0] + diff[0]]
            if otherTree[dir]["h"] < tree["height"]:
                tree[dir]["h"] = tree["height"]
                tree[dir]["dist"] = j
                tree["vis"] = True
            else:
                tree[dir]["h"] = otherTree[dir]["h"]
                tree[dir]["dist"] = dists[tree["height"]]
            for k in range(tree["height"]+1):
                dists[k] = 0

biggest = float("-inf")
for line in fixedGrid:
    for tree in line:
        v = 1
        for dir in dirs:
            v *= tree[dir]["dist"]
        if v > biggest:
            biggest = v
print(biggest)