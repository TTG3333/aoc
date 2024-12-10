with open("Input.txt", "tr") as F:
    lines = F.read().splitlines()

maxX = len(lines[0])
maxY = len(lines)
around = [[1, 0], [0, 1], [-1, 0], [0, -1]]
def checkAround(x, y, level):
    count = 0
    for xOff, yOff in around:
        newX = x + xOff
        newY = y + yOff
        if newX >= 0 and newX < maxX and newY >= 0 and newY < maxY:
            if lines[newY][newX] == str(level + 1):
                count += checkAround(newX, newY, level + 1) if level <= 7 else 1 # If level is 8 then level + 1 is 9
    return count

total = 0
for y, line in enumerate(lines):
    for x, char in enumerate(line):
        if char == "0":
            total += checkAround(x, y, 0)
print(total)