with open("Input.txt", "tr") as F:
    lines = [[[int(z) for z in y.split(",")] for y in x.split(" -> ")] for x in F.read().splitlines()]

xMax = yMax = 0
fixedLines = []
for line in lines:
    x1, y1, x2, y2 = line[0][0], line[0][1], line[1][0], line[1][1]
    xMax = max(xMax, x1, x2)
    yMax = max(yMax, y1, y2)
    if x1 == x2:
        lineType = "v"
        if y1 > y2:
            y1, y2 = y2, y1
    elif y1 == y2:
        lineType = "h"
        if x1 > x2:
            x1, x2 = x2, x1
    else:
        lineType = "d"
    line = {"x1": x1, "x2": x2, "y1": y1, "y2": y2, "type": lineType}
    fixedLines.append(line)

grid = [[0 for _ in range(xMax+1)] for _ in range(yMax+1)]
for line in fixedLines:
    if line["type"] == "h":
        for x in range(line["x1"], line["x2"]+1):
            grid[line["y1"]][x] += 1
    elif line["type"] == "v":
        for y in range(line["y1"], line["y2"]+1):
            grid[y][line["x1"]] += 1
    else:
        x1, x2, y1, y2 = line["x1"], line["x2"], line["y1"], line["y2"]
        lngth = abs(x1-x2) + 1
        if x1 > x2 and y1 > y2:
            for x in range(lngth):
                grid[y1-x][x1-x] += 1
        elif x1 > x2 and y1 < y2:
            for x in range(lngth):
                grid[y1+x][x1-x] += 1
        elif x1 < x2 and y1 > y2:
            for x in range(lngth):
                grid[y1-x][x1+x] += 1
        elif x1 < x2 and y1 < y2:
            for x in range(lngth):
                grid[y1+x][x1+x] += 1

count = 0
for y in grid:
    for x in y:
        if x >= 2:
            count += 1
print(count)