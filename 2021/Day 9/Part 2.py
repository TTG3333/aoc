from copy import deepcopy

with open("Input.txt", "tr") as F:
    points = [[[int(y), False] for y in x] for x in F.read().splitlines()]
around = [[-1, 0], [0, 1], [1, 0], [0, -1]]
maxX = len(points[0]) - 1
maxY = len(points) - 1
def checkAround(map, y, x):
    map[y][x][1] = True
    for z in around:
        xCoord = x + z[0]
        yCoord = y + z[1]
        if xCoord > maxX or xCoord < 0:
            continue
        elif yCoord > maxY or yCoord < 0:
            continue
        elif map[yCoord][xCoord][0] == 9 or map[yCoord][xCoord][1]:
            continue
        else:
            map[yCoord][xCoord][1] = True
            checkAround(map, yCoord, xCoord)

lowPoints = []
for y, row in enumerate(points):
    for x, location in enumerate(row):
        location = location[0]
        for z in around:
            xCoord = x + z[0]
            yCoord = y + z[1]
            if xCoord > maxX or xCoord < 0 or yCoord < 0 or yCoord > maxY:
                continue
            if location >= points[yCoord][xCoord][0]:
                break
        else:
            lowPoints.append([x, y])

result = []
for point in lowPoints:
    newMap = deepcopy(points)
    checkAround(newMap, point[1], point[0])
    count = 0
    for row in newMap:
        for cell in row:
            if cell[1]:
                count += 1
    result.append(count)
counter = 1
for x in sorted(result, reverse=True)[:3]:
    counter *= x
print(counter)