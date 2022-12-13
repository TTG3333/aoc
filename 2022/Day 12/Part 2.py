from string import ascii_lowercase

with open("Input.txt", "tr") as F:
    lines = F.read().splitlines()

startPos, endPos = None, None
grid = []
for y, line in enumerate(lines):
    if "E" in line:
        startPos = [line.find("E"), y]
    grid.append([{"height": ascii_lowercase.find(x), "dist": float("inf")} for x in line])
grid[startPos[1]][startPos[0]] = {"height": 25, "dist": 0}

unvisited = {(x, y) for x in range(len(grid[0])) for y in range(len(grid))}
current = tuple(startPos)
around = ((-1, 0), (0, 1), (1, 0), (0, -1))
while len(unvisited) > 0: # Dijkstra
    dist = grid[current[1]][current[0]]["dist"]
    elevation = grid[current[1]][current[0]]["height"]
    if elevation == 0:
        break
    for offset in around:
        newPos = [current[i] + offset[i] for i in range(2)]
        if newPos[0] < 0 or newPos[0] >= len(grid[0]) or newPos[1] < 0 or newPos[1] >= len(grid):
            continue
        if tuple(newPos) in unvisited:
            if grid[newPos[1]][newPos[0]]["height"] >= elevation - 1:
                newDist = grid[newPos[1]][newPos[0]]["dist"]
                grid[newPos[1]][newPos[0]]["dist"] = min(dist+1, newDist)
    unvisited.remove(tuple(current))
    if len(unvisited) > 0:
        current = min(unvisited, key=lambda a: grid[a[1]][a[0]]["dist"])
    else:
        break

print(dist)