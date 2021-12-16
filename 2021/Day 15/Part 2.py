from copy import deepcopy

with open("Input.txt", "tr") as F:
    cave = [[[int(y), float("inf"), False] for y in x] for x in F.read().splitlines()]
origCave = deepcopy(cave)
lastX = lastY = 0
for y in range(5):
    for x in range(5):
        if y == x == 0:
            continue
        if y != lastY:
            for row in origCave:
                cave.append([[(z[0]+x+y-1)%9+1, z[1], False] for z in row])
        elif x != lastX:
            for rowC, row in enumerate(origCave):
                cave[rowC+y*len(origCave)].extend([[(z[0]+x+y-1)%9+1, z[1], False] for z in row])
        lastX, lastY = x, y

around = [[0, 1], [1, 0], [-1, 0], [0, -1]]
maxX = len(cave[0]) - 1
maxY = len(cave) - 1
cave[0][0][1] = 0
checked = [[0, 0]]

def dijkstra(position):
    cave[position[1]][position[0]][2] = True
    checked.remove(position)
    if position == [maxX, maxY]:
        return
    for z in around:
        xCoord = z[0] + position[0]
        yCoord = z[1] + position[1]
        if xCoord < 0 or xCoord > maxX or yCoord < 0 or yCoord > maxY:
            continue
        if not cave[yCoord][xCoord][2]:
            cave[yCoord][xCoord][1] = min(cave[yCoord][xCoord][1], cave[position[1]][position[0]][1] + cave[yCoord][xCoord][0])
            if [xCoord, yCoord] not in checked:
                checked.append([xCoord, yCoord])

dijkstra([0, 0])
while not cave[maxY][maxX][2]:
    smallest = float("inf")
    for x, y in checked:
        if smallest == float("inf"):
            smallest = [x, y]
        else:
            if cave[y][x][1] < cave[smallest[1]][smallest[0]][1]:
                smallest = [x, y]
    dijkstra(smallest)

print(cave[maxY][maxX][1])