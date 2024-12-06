from copy import deepcopy

with open("Input.txt", "tr") as F:
    lines = [[char for char in line] for line in F.read().splitlines()]

position = []
direction = ""
for y, line in enumerate(lines):
    for char in "<>v^":
        if char in line:
            position = [line.index(char), y]
            direction = char
            break
    else:
        continue
    break

def checkPos(p):
    return p[0] >= 0 and p[0] < len(lines[0]) and p[1] >= 0 and p[1] < len(lines)

offsets = {">": [1, 0], "v": [0, 1], "<": [-1, 0], "^": [0, -1]}
nextDir = {">": "v", "v": "<", "<": "^", "^": ">"}
def checkLoop(position, direction, obstruction):
    path = set()
    newLines = deepcopy(lines)
    newLines[obstruction[1]][obstruction[0]] = "#"
    while checkPos(position):
        if (tuple(position), direction) in path:
            return True
        path.add((tuple(position), direction))
        newPos = [position[x] + offsets[direction][x] for x in range(2)]
        while checkPos(newPos) and newLines[newPos[1]][newPos[0]] == "#":
            direction = nextDir[direction]
            newPos = [position[x] + offsets[direction][x] for x in range(2)]
        position = newPos
    return False

total = 0
for y in range(len(lines)):
    for x in range(len(lines[0])):
        if [x, y] != position and lines[y][x] != "#": # No obstruction at start location
            total += checkLoop(position, direction, [x, y])

print(total)