with open("Input.txt", "tr") as F:
    lines = F.read().splitlines()

around = [[-1, -1], [-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1]]

rows = len(lines)
cols = len(lines[0])
total = 0
for i, line in enumerate(lines):
    for j, c in enumerate(line):
        if lines[i][j] != "@":
            continue
        count = 0
        for dx, dy in around:
            x, y = j + dx, i + dy
            if x < 0 or x >= cols or y < 0 or y >= rows:
                continue
            if lines[y][x] == "@":
                count += 1
        if count < 4:
            total += 1
print(total)