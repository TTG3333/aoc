with open("Input.txt", "tr") as F:
    lines = F.read().splitlines()

test = "XMAS"

def checkLetter(y, x, pos, directions):
    around = [[0, -1], [-1, -1], [-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1]]
    count = 0
    for k in directions:
        newX, newY = x+around[k][0], y+around[k][1]
        if newX < 0 or newX >= len(lines[y]) or newY < 0 or newY >= len(lines):
            continue
        if lines[newY][newX] == test[pos]:
            if pos == 3:
                count += 1
            else:
                count += checkLetter(newY, newX, pos+1, [k])
    return count

total = 0
allDirs = list(range(8))
for y, line in enumerate(lines):
    for x, char in enumerate(line):
        if char == "X":
            total += checkLetter(y, x, 1, allDirs)
print(total)