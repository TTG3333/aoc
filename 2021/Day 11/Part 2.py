from copy import deepcopy

with open("Input.txt", "tr") as F:
    octopi = [[int(y) for y in x] for x in F.read().splitlines()]
around = [[-1, -1], [0, -1], [1, -1], [1, 0], [1, 1], [0, 1], [-1, 1], [-1, 0]]

maxX = len(octopi[0]) - 1
maxY = len(octopi) - 1

def checkOctopus(grid, x, y, checked):
    for z in around:
        xCoord = x + z[0]
        yCoord = y + z[1]
        if xCoord < 0 or xCoord > maxX or yCoord < 0 or yCoord > maxY:
            continue
        if [xCoord, yCoord] in checked:
            continue
        if grid[yCoord][xCoord] < 9:
            grid[yCoord][xCoord] += 1
        elif grid[yCoord][xCoord] == 9:
            grid[yCoord][xCoord] += 1
            checked.append([xCoord, yCoord])
            checkOctopus(grid, xCoord, yCoord, checked)
        else:
            checked.append([xCoord, yCoord])
            checkOctopus(grid, xCoord, yCoord, checked)

step = 0
while True:
    step += 1
    for y in range(maxY + 1):
        for x in range(maxX + 1):
            octopi[y][x] += 1
    flashed = []
    for y, row in enumerate(octopi):
        for x, octopus in enumerate(row):
            if octopus > 9 and [x, y] not in flashed:
                flashed.append([x, y])
                checkOctopus(octopi, x, y, flashed)
    for x, y in flashed:
        octopi[y][x] = 0
    if len(flashed) == len(octopi) * len(octopi[0]):
        break
print(step)