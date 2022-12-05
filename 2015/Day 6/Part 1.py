with open("Input.txt", "tr") as F:
    insts = F.read().splitlines()
lights = [[False]*1000 for _ in range(1000)]

for inst in insts:
    firstCoords, lastCoords = [[int(y) for y in x.split(",")] for x in inst.split(" ")[-3::2]]
    if inst.startswith("turn on"):
        for row in range(firstCoords[0], lastCoords[0]+1):
            for col in range(firstCoords[1], lastCoords[1]+1):
                lights[row][col] = True
    elif inst.startswith("turn off"):
        for row in range(firstCoords[0], lastCoords[0]+1):
            for col in range(firstCoords[1], lastCoords[1]+1):
                lights[row][col] = False
    elif inst.startswith("toggle"):
        for row in range(firstCoords[0], lastCoords[0]+1):
            for col in range(firstCoords[1], lastCoords[1]+1):
                lights[row][col] = not lights[row][col]

count = 0
for row in lights:
    count += row.count(True)
print(count)