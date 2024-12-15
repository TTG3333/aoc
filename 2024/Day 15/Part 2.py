with open("Input.txt", "tr") as F:
    lines = F.read().splitlines()

grid = []
robotPos = []
for movementIndex, line in enumerate(lines):
    if line == "":
        movementIndex += 1
        break
    newLine = []
    for char in line:
        match char:
            case "#":
                newLine.extend(["#", "#"])
            case "O":
                newLine.extend(["[", "]"])
            case ".":
                newLine.extend([".", "."])
            case "@":
                newLine.extend(["@", "."])
    grid.append(newLine)    
    if "@" in newLine:
        robotPos = [newLine.index("@"), movementIndex]

maxX = len(grid[0])
maxY = len(grid)
def checkCoords(x, y):
    return x >= 0 and x < maxX and y >= 0 and y < maxY

directions = {">": [1, 0], "v": [0, 1], "<": [-1, 0], "^": [0, -1]}
def pushBox(boxX, boxY, dir, check=False): # boxX and boxY are for the left half of the box, check is only used if direction is up/down, if check is true then nothing will be moved, it will only return t/f if stuff can move
    xOff, yOff = directions[dir]
    newX, newY = boxX + xOff, boxY + yOff
    if dir in "<>":
        if dir == "<": # We want to move the right edge of the box as well
            newX += 1
        toPush = 0
        while checkCoords(newX, newY) and grid[newY][newX] != "#":
            if grid[newY][newX] != ".":
                toPush += 1
                newX += xOff
                newY += yOff
            else:
                while toPush >= 0:
                    oldX = newX - xOff
                    oldY = newY - yOff
                    grid[newY][newX] = grid[oldY][oldX]
                    grid[oldY][oldX] = "."
                    newX, newY = oldX, oldY
                    toPush -= 1
                break
        else:
            return False
    else:
        if grid[newY][newX] != "#" and grid[newY][newX+1] != "#":
            for side in range(2):
                match grid[newY][newX+side]:
                    case "[":
                        if not pushBox(newX+side, newY, dir, True):
                            return False
                    case "]":
                        if not pushBox(newX+side-1, newY, dir, True):
                            return False
            if check:
                return True
            for side in range(2):
                match grid[newY][newX+side]:
                    case "[":
                        pushBox(newX+side, newY, dir)
                    case "]":
                        pushBox(newX+side-1, newY, dir)
            grid[newY][newX] = "["
            grid[newY][newX+1] = "]"
            grid[boxY][boxX] = "."
            grid[boxY][boxX+1] = "."
        else:
            return False
    return True


movements = "".join(lines[movementIndex:])
for movement in movements:
    xOff, yOff = directions[movement]
    newX, newY = robotPos[0] + xOff, robotPos[1] + yOff
    match grid[newY][newX]:
        case "[":
            if not pushBox(newX, newY, movement):
                continue
        case "]":
            if not pushBox(newX-1, newY, movement):
                continue
        case "#":
            continue
    grid[newY][newX] = "@"
    grid[robotPos[1]][robotPos[0]] = "."
    robotPos = [newX, newY]

total = 0
for y, line in enumerate(grid):
    for x, char in enumerate(line):
        if char == "[":
            total += 100*y + x
print(total)