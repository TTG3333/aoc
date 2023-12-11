with open("Input.txt", "tr") as F:
    lines = F.read().splitlines()

around = [[(0, 1), "-J7"], [(1, 0), "|JL"], [(0, -1), "-LF"], [(-1, 0), "|7F"]]
letterDirs = {}
for dir, pipes in around:
    for char in pipes:
        if char in letterDirs:
            letterDirs[char].append(tuple(-x for x in dir))
        else:
            letterDirs[char] = [tuple(-x for x in dir)]

sCoords = None
for i, line in enumerate(lines):
    loc = line.find("S")
    if loc != -1:
        sCoords = [i, loc]
        break

movements = []
firstPos, secondPos = [list(sCoords), None, "S"], [list(sCoords), None, "S"]
for direction, vPipes in around:
    currentPos = [sCoords[0] + direction[0], sCoords[1] + direction[1]]
    if currentPos[0] >= 0 and currentPos[0] < len(lines) and currentPos[1] >= 1 and currentPos[1] < len(lines[0]):
        currentVal = lines[currentPos[0]][currentPos[1]]
        if currentVal in vPipes:
            if firstPos[2] == "S":
                firstPos = [currentPos.copy(), tuple(-x for x in direction), currentVal]
            else:
                secondPos = [currentPos.copy(), tuple(-x for x in direction), currentVal]
            movements.append(direction)

sVal = ""
for key, val in letterDirs.items():
    if set(movements) == set(val):
        sVal = key
        break

def advance(position):
    pos, prevDir, val = position
    for direction in letterDirs[val]:
        if direction != prevDir:
            currentPos = [pos[0] + direction[0], pos[1] + direction[1]]
            currentVal = lines[currentPos[0]][currentPos[1]]
            return [currentPos.copy(), tuple(-x for x in direction), currentVal]

linePoints = {tuple(sCoords): sVal, tuple(firstPos[0]): firstPos[2], tuple(secondPos[0]): secondPos[2]}
while firstPos[0] != secondPos[0]:
    firstPos = advance(firstPos)
    secondPos = advance(secondPos)
    linePoints[tuple(firstPos[0])] =  firstPos[2]
    linePoints[tuple(secondPos[0])] = secondPos[2]

inside = set()
for i in range(len(lines)):
    inFig = False
    inLine = False
    start = ""
    for j in range(len(lines[i])):
        if (i, j) in linePoints:
            point = linePoints[(i, j)]
            if inLine:
                if point != "-":
                    if (start == "L" and point == "7") or (start == "F" and point == "J"):
                        inFig = not inFig
                    inLine = False
            elif point == "|":
                inFig = not inFig
            elif not inLine:
                start = point
                inLine = True
        elif inFig:
            inside.add((i, j))
        
print(len(inside))