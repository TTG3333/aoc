with open("Input.txt", "tr") as F:
    data = F.read().splitlines()

dots = []
for y, x in enumerate(data):
    if x == "":
        foldStart = y + 1
        break
    dots.append([int(z) for z in x.split(",")])
maxX = max([x[0] for x in dots]) + 1
maxY = max([x[1] for x in dots]) + 1
folds = [[x.split(" ")[2].split("=")[0], int(x.split(" ")[2].split("=")[1])] for x in data[foldStart:]]

grid = [[False for _ in range(maxX)] for _ in range(maxY)]
for dot in dots:
    grid[dot[1]][dot[0]] = True

for fold in folds:
    if fold[0] == "x":
        for y, line in enumerate(grid):
            for x, dot in enumerate(line[fold[1] + 1:], start=fold[1] + 1):
                if dot == True:
                    grid[y][fold[1]*2-x] = True
            grid[y] = grid[y][:fold[1]]
    else:
        for y, line in enumerate(grid[fold[1] + 1:], start=fold[1] + 1):
            for x, dot in enumerate(line):
                if dot == True:
                    grid[fold[1]*2-y][x] = True
        grid = grid[:fold[1]]
for line in grid:
    for dot in line:
        print("#" if dot else ".", end="")
    print()