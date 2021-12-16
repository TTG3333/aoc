with open("Input.txt", "tr") as F:
    cave = [[[int(y), float("inf")] for y in x] for x in F.read().splitlines()]
around = [[0, 1], [1, 0], [-1, 0], [0, -1]]
maxX = len(cave[0]) - 1
maxY = len(cave) - 1
unchecked = []
cave[0][0][1] = 0
for x in range(maxX + 1):
    for y in range(maxY + 1):
        unchecked.append([x, y])

def dijkstra(position):
    unchecked.remove(position)
    if position == [maxX, maxY]:
        return
    results = []
    for z in around:
        xCoord = z[0] + position[0]
        yCoord = z[1] + position[1]
        if xCoord < 0 or xCoord > maxX or yCoord < 0 or yCoord > maxY:
            continue
        if [xCoord, yCoord] not in unchecked:
            continue
        cave[yCoord][xCoord][1] = min(cave[yCoord][xCoord][1], cave[position[1]][position[0]][1] + cave[yCoord][xCoord][0])
        results.append([xCoord, yCoord, cave[yCoord][xCoord][1]])

dijkstra([0, 0])
while [maxX, maxY] in unchecked:
    smallest = float("inf")
    for x, y in unchecked:
        if smallest == float("inf"):
            smallest = [x, y]
        else:
            if cave[y][x][1] < cave[smallest[1]][smallest[0]][1]:
                smallest = [x, y]
    dijkstra(smallest)

print(cave[maxY][maxX][1])