with open("Input.txt", "tr") as F:
    lines = F.read().splitlines()

around = [[-1, -1], [-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1]]

rows = len(lines)
cols = len(lines[0])
total = 0
removed = True
while removed:
    removed = False
    to_remove = []
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
                to_remove.append((i, j))
    for i, j in to_remove:
        lines[i] = lines[i][:j] + "." + lines[i][j+1:]
    if to_remove:
        removed = True
print(total)