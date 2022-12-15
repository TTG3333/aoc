with open("Input.txt", "tr") as F:
    lines = F.read().splitlines()

sensors = []
for line in lines:
    line = line.split(" ")
    x = int(line[2][2:-1])
    y = int(line[3][2:-1])
    beaconX = int(line[-2][2:-1])
    beaconY = int(line[-1][2:])
    dist = abs(x - beaconX) + abs(y - beaconY)
    sensors.append({"x": x, "y": y, "beaconX": beaconY, "beaconY": beaconY, "dist": dist})

val = 2000000
xCoords = set()
toRem = set()
for sens in sensors:
    yDist = abs(sens["y"] - val)
    if yDist > sens["dist"]:
        continue
    remDist = sens["dist"] - yDist
    xCoord = sens["x"]
    for i in range(xCoord - remDist, xCoord + remDist + 1):
        xCoords.add(i)
    if sens["beaconY"] == val:
        toRem.add(sens["beaconX"])
for v in toRem:
    if v in xCoords:
        xCoords.remove(v)
print(len(xCoords))