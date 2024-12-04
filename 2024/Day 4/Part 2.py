with open("Input.txt", "tr") as F:
    lines = F.read().splitlines()

def checkLetter(y, x):
    diags = [[[-1, -1], [1, 1]], [[-1, 1], [1, -1]]]
    count = 0
    for d in diags:
        match = 0
        for xOff, yOff in d:
            newX = x + xOff
            newY = y + yOff
            char = lines[newY][newX]
            match += 1 if char == "M" else 2 if char == "S" else 0
        count += match == 3
    return count == 2

total = 0
for y, line in enumerate(lines[1:-1], start=1):
    for x, char in enumerate(line[1:-1], start=1):
        if char == "A":
            total += checkLetter(y, x)
print(total)