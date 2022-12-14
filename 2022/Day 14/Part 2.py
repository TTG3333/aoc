with open("Input.txt", "tr") as F:
    lines = F.read().splitlines()

grid = {} # list of columns
for line in lines:
    currentPos = None
    for pos in line.split(" -> "):
        pos = [int(x) for x in pos.split(",")]
        if currentPos == None:
            currentPos = pos
            continue
        if currentPos[0] == pos[0]:
            if pos[0] not in grid:
                grid[pos[0]] = {}
            for i in range(min(currentPos[1], pos[1]), max(currentPos[1], pos[1])+1):
                grid[pos[0]][i] = True
        elif currentPos[1] == pos[1]:
            for i in range(min(currentPos[0], pos[0]), max(currentPos[0], pos[0])+1):
                if i not in grid:
                    grid[i] = {}
                grid[i][pos[1]] = True
        currentPos = pos

xOffset = min(grid.keys())
xCount = max(grid.keys())+1-xOffset
maxY = max(max(grid.values(), key=lambda a: max(a.keys())).keys()) + 2
fixedGrid = {i:["."]*(maxY+1) for i in range(xCount)} # list of columns
for k, v in grid.items():
    for k2 in v.keys():
        fixedGrid[k-xOffset][k2] = "#"
    fixedGrid[k-xOffset][-1] = "#"

grid = fixedGrid
count = 0
while True:
    start = 500-xOffset
    if grid[start][0] == "#":
        break
    count += 1
    pos = [start, 0]
    while True:
        if pos[0]-1 not in grid:
            grid[pos[0]-1] = ["."]*(maxY+1)
            grid[pos[0]-1][-1] = "#"
        if pos[0]+1 not in grid:
            grid[pos[0]+1] = ["."]*(maxY+1)
            grid[pos[0]+1][-1] = "#"
        if grid[pos[0]][pos[1]+1] != "#":
            pos[1] += 1
        elif grid[pos[0]-1][pos[1]+1] != "#":
            pos[0] -= 1
            pos[1] += 1
        elif grid[pos[0]+1][pos[1]+1] != "#":
            pos[0] += 1
            pos[1] += 1
        else:
            grid[pos[0]][pos[1]] = "#"
            break
print(count)