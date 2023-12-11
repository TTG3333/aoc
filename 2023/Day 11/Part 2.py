with open("Input.txt", "tr") as F:
    lines = F.read().splitlines()

galaxyCoords = []
emptyRows = set()
emptyCols = set(range(len(lines[0])))
for i, line in enumerate(lines):
    noGal = True
    for j, char in enumerate(line):
        if char == "#":
            galaxyCoords.append((i, j))
            noGal = False
            if j in emptyCols:
                emptyCols.remove(j)
    if noGal:
        emptyRows.add(i)

total = 0
for i, galaxy in enumerate(galaxyCoords[:-1]):
    for galaxy2 in galaxyCoords[i+1:]:
        diffs = [abs(galaxy[j] - galaxy2[j]) for j in range(2)]
        rows, cols = [set(range(min(galaxy[j], galaxy2[j]) + 1, min(galaxy[j], galaxy2[j]) + diffs[j])) for j in range(2)]
        extraRows = rows&emptyRows
        extraCols = cols&emptyCols
        total += sum(diffs) + 999999 * (len(extraCols) + len(extraRows))
print(total)