with open("Input.txt", "tr") as F:
    map = [[int(y) for y in x] for x in F.read().splitlines()]

around = [[-1, 0], [0, 1], [1, 0], [0, -1]]
rskLvl = 0
for y, row in enumerate(map):
    for x, location in enumerate(row):
        for z in around:
            xCoord = x + z[0]
            yCoord = y + z[1]
            if xCoord > 99 or xCoord < 0 or yCoord < 0 or yCoord > 99:
                continue
            if location >= map[yCoord][xCoord]:
                break
        else:
            rskLvl += location + 1
print(rskLvl)