with open("Input.txt", "tr") as F:
    insts = F.read()
coords = [[0, 0], [0, 0]] # x(rightwards), y(upwards)
visited = {tuple(coords[0])}
for i, inst in enumerate(insts):
    currentCoords = coords[i%2]
    if inst == "^": # North
        currentCoords[1] += 1
    elif inst == "<": # West
        currentCoords[0] -= 1
    elif inst == "v": # South
        currentCoords[1] -= 1
    elif inst == ">": # East
        currentCoords[0] += 1
    visited.add(tuple(currentCoords))
print(len(visited))