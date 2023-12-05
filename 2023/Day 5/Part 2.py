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
def feedForward(start, length, mapIndex):
    global lowest
    if mapIndex >= len(maps):
        if start < lowest:
            lowest = start
        return
    currentMap = maps[mapIndex]
    while length > 0:
        for group in currentMap:
            if start >= group[1] and start < group[1] + group[2]:
                newLength = min(length, group[2], group[1] + group[2] - start)
                offset = group[0] - group[1]
                feedForward(start + offset, newLength, mapIndex + 1)
                length -= newLength
                start += newLength
                break
        else:
            lowestStart = (float("inf"),)*3
            for group in currentMap:
                if group[1] - start >= 0 and group[1] - start < lowestStart[1] - start:
                    lowestStart = group
            newLength = min(length, lowestStart[1] - start)
            feedForward(start, newLength, mapIndex + 1)
            length -= newLength
            start += newLength

for i in range(0, len(seeds), 2):
    start, length = seeds[i: i+2]
    feedForward(start, length, 0)

print(lowest)