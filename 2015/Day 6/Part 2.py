with open("Input.txt", "tr") as F:
    insts = F.read().splitlines()
lights = [[0]*1000 for _ in range(1000)]

for inst in insts:
    firstCoords, lastCoords = [[int(y) for y in x.split(",")] for x in inst.split(" ")[-3::2]]
    if inst.startswith("turn on"):
        for row in range(firstCoords[0], lastCoords[0]+1):
            for col in range(firstCoords[1], lastCoords[1]+1):
                lights[row][col] += 1
    elif inst.startswith("turn off"):
        for row in range(firstCoords[0], lastCoords[0]+1):
            for col in range(firstCoords[1], lastCoords[1]+1):
                if lights[row][col] > 0:
                    lights[row][col] -= 1
    elif inst.startswith("toggle"):
        for row in range(firstCoords[0], lastCoords[0]+1):
            for col in range(firstCoords[1], lastCoords[1]+1):
                lights[row][col] += 2

count = 0
for row in lights:
    count += sum(row)
print(count)