from string import digits

with open("Input.txt", "tr") as F:
    lines = F.read().splitlines()

around = [[-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1]]

total = 0
for i, line in enumerate(lines):
    num_str = ""
    part = False
    for j, char in enumerate(line):
        if char in digits:
            num_str += char
            for xOff, yOff in around:
                newX = j + xOff
                newY = i + yOff
                if newX >= 0 and newX < len(line) and newY >= 0 and newY < len(lines):
                    if lines[newY][newX] != "." and lines [newY][newX] not in digits:
                        part = True
        elif num_str != "":
            total += int(num_str) if part else 0
            num_str = ""
            part = False
    if num_str != "":
        total += int(num_str) if part else 0
        num_str = ""
        part = False
print(total)