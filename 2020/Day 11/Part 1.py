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
                for z in seatsAround:
                    if row + z[0] >= rowCount or row + z[0] < 0:
                        continue
                    elif col + z[1] >= colCount or col + z[1] < 0:
                        continue
                    elif grid[row+z[0]][col+z[1]] == True:
                        break
                else:
                    updated_grid[row][col] = not updated_grid[row][col]
                    changes += 1
            elif y == True:
                occupiedCount = 0
                for z in seatsAround:
                    if row + z[0] >= rowCount or row + z[0] < 0:
                        continue
                    elif col + z[1] >= colCount or col + z[1] < 0:
                        continue
                    elif grid[row+z[0]][col+z[1]] == True:
                        occupiedCount += 1
                if occupiedCount >= 4:
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