with open("Input.txt", "tr") as F:
    lines = F.read().splitlines()

maxY = len(lines)
maxX = len(lines[0])
antinodes = set()
antennae = {}
for y, line in enumerate(lines):
    for x, char in enumerate(line):
        if char != ".":
            if char in antennae:
                antennae[char].append([x, y])
            else:
                antennae[char] = [[x, y]]

def checkCoords(x, y):
    return x >= 0 and x < maxX and y >= 0 and y < maxY

for freq, positions in antennae.items():
    if len(positions) <= 1:
        continue
    for i in range(len(positions) - 1): # First antenna
        if tuple(positions[i]) not in antinodes: # Antinode at the antenna
            antinodes.add(tuple(positions[i]))
        for j in range(i+1, len(positions)): # Second antenna
            if tuple(positions[j]) not in antinodes: # Antinode at the antenna
                antinodes.add(tuple(positions[j]))
            offset = [positions[j][k] - positions[i][k] for k in range(2)] # Assume no antinode between the antennae, this is the vector from i to j
            newPos = [positions[i][k] - offset[k] for k in range(2)] # Check before i
            while checkCoords(*newPos): # CHeck multiples 
                if tuple(newPos) not in antinodes:
                    antinodes.add(tuple(newPos))
                newPos[0] -= offset[0]
                newPos[1] -= offset[1]
            newPos = [positions[j][k] + offset[k] for k in range(2)] # Check after j
            while checkCoords(*newPos): # CHeck multiples 
                if tuple(newPos) not in antinodes:
                    antinodes.add(tuple(newPos))
                newPos[0] += offset[0]
                newPos[1] += offset[1]
print(len(antinodes))