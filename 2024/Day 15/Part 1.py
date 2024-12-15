with open("Input.txt", "tr") as F:
    lines = F.read().splitlines()

grid = []
robotPos = []
for movementIndex, line in enumerate(lines):
    if line == "":
        movementIndex += 1
        break
    grid.append([char for char in line])
    if "@" in line:
        robotPos = [line.find("@"), movementIndex]

maxX = len(grid[0])
maxY = len(grid)
def checkCoords(x, y):
    return x >= 0 and x < maxX and y >= 0 and y < maxY

movements = "".join(lines[movementIndex:])
direction = {">": [1, 0], "v": [0, 1], "<": [-1, 0], "^": [0, -1]}
for movement in movements:
    xOff, yOff = direction[movement]
    newX, newY = robotPos[0] + xOff, robotPos[1] + yOff
    boxes = 0
    while checkCoords(newX, newY) and grid[newY][newX] != "#":
        if grid[newY][newX] != ".":
            boxes += 1
            newX += xOff
            newY += yOff
        else:
            while boxes >= 0:
                if boxes == 0:
                    robotPos = [newX, newY]
                oldX = newX - xOff
                oldY = newY - yOff
                grid[newY][newX] = grid[oldY][oldX]
                grid[oldY][oldX] = "."
                newX, newY = oldX, oldY
                boxes -= 1
            break

total = 0
for y, line in enumerate(grid):
    for x, char in enumerate(line):
        if char == "O":
            total += 100*y + x
print(total)