with open("Input.txt", "tr") as F:
    lines = F.read().splitlines()

visited = set()
position = []
direction = ""
for y, line in enumerate(lines):
    for char in "<>v^":
        if char in line:
            position = [line.find(char), y]
            direction = char
            break
    else:
        continue
    break

offsets = {">": [1, 0], "v": [0, 1], "<": [-1, 0], "^": [0, -1]}
nextDir = {">": "v", "v": "<", "<": "^", "^": ">"}
while position[0] >= 0 and position[0] < len(lines[0]) and position[1] >= 0 and position[1] < len(lines):
    visited.add(tuple(position))
    newPos = [position[x] + offsets[direction][x] for x in range(2)]
    while newPos[0] >= 0 and newPos[0] < len(lines[0]) and newPos[1] >= 0 and newPos[1] < len(lines) and lines[newPos[1]][newPos[0]] == "#":
        direction = nextDir[direction]
        newPos = [position[x] + offsets[direction][x] for x in range(2)]
    position = newPos
    
print(len(visited))