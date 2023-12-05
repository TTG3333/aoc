with open("Input.txt", "tr") as F:
    lines = F.read().splitlines()

seeds = [int(x) for x in lines[0].split(": ")[1].split(" ")]
lines = lines[3:] # Now starts at seed to soil
maps = []
currentMap = []
skip = 0
for line in lines:
    if skip > 0:
        skip -= 1
        continue
    if line != "":
        dest, source, length = [int(x) for x in line.split(" ")]
        currentMap.append((dest, source, length))
    else:
        maps.append(currentMap.copy())
        currentMap = []
        skip = 1
maps.append(currentMap.copy())

lowest = float("inf")
for seed in seeds:
    currentVal = seed
    for cMap in maps:
        for group in cMap:
            if currentVal >= group[1] and currentVal < group[1] + group[2]:
                currentVal = group[0] + currentVal - group[1]
                break
    if currentVal < lowest:
        lowest = currentVal
print(lowest)