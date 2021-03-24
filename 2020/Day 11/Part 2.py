with open("Input.txt", "tr") as F:
    rows = F.read().splitlines()
grid = []
for x in rows:
    fixed_column = []
    for y in x:
        if y == ".":
            fixed_column.append(None)
        elif y == "#":
            fixed_column.append(True)
        elif y == "L":
            fixed_column.append(False)
    grid.append(fixed_column)

seatsAround = [
    [0,1],
    [1,1],
    [1,0],
    [1,-1],
    [0,-1],
    [-1,-1],
    [-1,0],
    [-1,1]
]

def copyList(copyFrom):
    output = []
    for x in copyFrom:
        row = []
        for y in x:
            if y == True:
                row.append(True)
            elif y == False:
                row.append(False)
            elif y == None:
                row.append(None)
        output.append(row)
    return output

updated_grid = []
rowCount = len(grid)
colCount = len(grid[0])
while True:
    updated_grid = copyList(grid)
    changes = 0
    for row, x in enumerate(grid):
        for col, y in enumerate(x):
            if y == False:
                occupiedCount = 0
                for z in seatsAround:
                    pos = [row + z[0], col + z[1]]
                    if pos[0] >= rowCount or pos[0] < 0:
                        continue
                    elif pos[1] >= colCount or pos[1] < 0:
                        continue
                    while grid[pos[0]][pos[1]] == None:
                        pos[0] += z[0]
                        pos[1] += z[1]
                        if pos[0] >= rowCount or pos[0] < 0:
                            break
                        elif pos[1] >= colCount or pos[1] < 0:
                            break
                    else:
                        if grid[pos[0]][pos[1]] == True:
                            occupiedCount += 1
                if occupiedCount == 0:
                    updated_grid[row][col] = not updated_grid[row][col]
                    changes += 1
            elif y == True:
                occupiedCount = 0
                for z in seatsAround:
                    pos = [row + z[0], col + z[1]]
                    if pos[0] >= rowCount or pos[0] < 0:
                        continue
                    elif pos[1] >= colCount or pos[1] < 0:
                        continue
                    while grid[pos[0]][pos[1]] == None:
                        pos[0] += z[0]
                        pos[1] += z[1]
                        if pos[0] >= rowCount or pos[0] < 0:
                            break
                        elif pos[1] >= colCount or pos[1] < 0:
                            break
                    else:
                        if grid[pos[0]][pos[1]] == True:
                            occupiedCount += 1
                if occupiedCount >= 5:
                    updated_grid[row][col] = not updated_grid[row][col]
                    changes += 1
    if changes == 0:
        break
    grid = copyList(updated_grid)

occupied = 0
for x in grid:
    for y in x:
        if y == True:
            occupied += 1
print(occupied)