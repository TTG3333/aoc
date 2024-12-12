with open("Input.txt", "tr") as F:
    lines = F.read().splitlines()

maxX = len(lines[0])
maxY = len(lines[1])
def checkCoords(x, y):
    return x >= 0 and x < maxX and y >= 0 and y < maxY

around = [[1, 0], [0, 1], [-1, 0], [0, -1]]
def checkNext(x, y, plant, checked):
    checked.add((x, y))
    area = 1
    perimeter = 0
    for xOff, yOff in around:
        newX = x + xOff
        newY = y + yOff
        if checkCoords(newX, newY) and lines[newY][newX] == plant:
            if (newX, newY) not in checked:
                returned = checkNext(newX, newY, plant, checked)
                area += returned[0]
                perimeter += returned[1]
        else: # We have a plot boundary, so increase the perimeter
            perimeter += 1
    return (area, perimeter)

total = 0
checked = set()
for y, line in enumerate(lines):
    for x, char in enumerate(line):
        if (x, y) not in checked: # checkNext will add all plots of a region to checked, so whenever we have a coordinate not in checked, we know it's a new region
            returned = checkNext(x, y, char, checked)
            total += returned[0] * returned[1]
print(total)