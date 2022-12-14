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
maxY = max(max(grid.values(), key=lambda a: max(a.keys())).keys())
fixedGrid = [["."]*xCount for _ in range(maxY+1)] # list of rows
for k, v in grid.items():
    for k2 in v.keys():
        fixedGrid[k2][k-xOffset] = "#"

grid = fixedGrid
start = 500-xOffset
doubleBreak = False
count = 0
while True:
    count += 1
    pos = [start, 0]
    while True:
        if pos[1] >= maxY or pos[0] < 0 or pos[0] >= xCount:
            count -= 1
            doubleBreak = True
            break
        if grid[pos[1]+1][pos[0]] != "#":
            pos[1] += 1
        elif pos[0] == 0:
            count -= 1
            doubleBreak = True
            break
        elif grid[pos[1]+1][pos[0]-1] != "#":
            pos[0] -= 1
            pos[1] += 1
        elif pos[0] == xCount-1:
            count -= 1
            doubleBreak = True
            break
        elif grid[pos[1]+1][pos[0]+1] != "#":
            pos[0] += 1
            pos[1] += 1
        else:
            grid[pos[1]][pos[0]] = "#"
            break
    if doubleBreak:
        break
print(count)