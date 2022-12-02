with open("Input.txt", "tr") as F:
    insts = F.read()
coords = [0, 0] # x(rightwards), y(upwards)
visited = {tuple(coords)}
for inst in insts:
    if inst == "^": # North
        coords[1] += 1
    elif inst == "<": # West
        coords[0] -= 1
    elif inst == "v": # South
        coords[1] -= 1
    elif inst == ">": # East
        coords[0] += 1
    visited.add(tuple(coords))
print(len(visited))