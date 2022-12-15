with open("Input.txt", "tr") as F:
    lines = F.read().splitlines()

def manhattan(x1, y1, x2, y2):
    return abs(x1-x2) + abs(y1-y2)

sensors = []
for line in lines:
    line = line.split(" ")
    x = int(line[2][2:-1])
    y = int(line[3][2:-1])
    beaconX = int(line[-2][2:-1])
    beaconY = int(line[-1][2:])
    dist = abs(x - beaconX) + abs(y - beaconY)
    sensors.append({"x": x, "y": y, "beaconX": beaconY, "beaconY": beaconY, "dist": dist})

maxPos = 4000000
finalPos = []
for y in range(maxPos+1):
    impossible = []
    for sens in sensors:
        yDist = abs(sens["y"] - y)
        if yDist > sens["dist"]:
            continue
        remDist = sens["dist"] - yDist
        xCoord = sens["x"]
        if xCoord - remDist > maxPos or xCoord + remDist < 0:
            continue
        impossible.append([max(0, xCoord - remDist), min(maxPos, xCoord + remDist)])
    impossible.sort(key=lambda a: a[0])
    current = impossible[0]
    for imp in impossible[1:]:
        if current[1]+1 >= imp[0]:
            current[1] = max(imp[1], current[1])
        else:
            finalPos = [current[1]+1, y]
            break
    else:
        continue
    break
print(finalPos[0]*4000000+finalPos[1])