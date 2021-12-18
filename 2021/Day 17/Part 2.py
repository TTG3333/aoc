with open("Input.txt", "tr") as F:
    data = [[int(y) for y in x.split("..")] for x in F.read()[15:].split(", y=")]
minX = 0
while (minX**2+minX)//2 < data[0][0]:
    minX += 1
maxX = data[0][1]
minY = data[1][0]
maxY = -minY - 1
xVals = list(range(data[0][0], maxX+1))
yVals = list(range(minY, data[1][1]+1))
count = 0
for x in range(minX, maxX+1):
    for y in range(minY, maxY+1):
        xInc = x
        xCoord = yCoord = 0
        while True:
            xCoord += xInc
            yCoord += y
            if xInc > 0:
                xInc -= 1
            y -= 1
            if (xCoord in xVals) and (yCoord in yVals):
                count += 1
                break
            if xCoord > maxX or yCoord < minY:
                break
print(count)