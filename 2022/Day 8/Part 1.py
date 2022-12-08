with open("Input.txt", "tr") as F:
    grid = F.read().splitlines()

fixedGrid = []
for line in grid:
    fixedGrid.append([{"height": int(x), "up": float("inf"), "down": float("inf"), "left": float("inf"), "right": float("inf"), "vis": False} for x in line])
size = len(fixedGrid) # We have a square
dirs = {"up": (0, -1), "down": (0, 1), "left": (-1, 0), "right": (1, 0)}

for dir, diff in dirs.items():
    for i in range(size):
        val = float("inf")
        for j in range(size):
            if dir  == "down":
                pos = [i, size - j - 1]
            elif dir == "up":
                pos = [i, j]
            elif dir == "right":
                pos = [size - j - 1, i]
            elif dir == "left":
                pos = [j, i]
            tree = fixedGrid[pos[0]][pos[1]]
            if j == 0:
                tree[dir] = tree["height"]
                tree["vis"] = True
                continue
            otherTree = fixedGrid[pos[0] + dirs[dir][0]][pos[1] + dirs[dir][1]]
            if otherTree[dir] < tree["height"]:
                tree[dir] = tree["height"]
                tree["vis"] = True
            else:
                tree[dir] = otherTree[dir]

count = 0
for row in fixedGrid:
    for tree in row:
        count += 1 if tree["vis"] else 0
print(count)