from copy import deepcopy
import re

with open("Input.txt", "tr") as F:
    lines = F.read().splitlines()

robots = []
for line in lines:
    robot = {}
    matches = [int(x) for x in re.match(r"^p=([\d-]+),([\d-]+) v=([\d-]+),([\d-]+)$", line).groups()]
    robot["p"] = matches[0], matches[1]
    robot["v"] = matches[2], matches[3]
    robots.append(robot)

limits = [101, 103]
symScore = lowestSymScore = float("inf") # The closer it is to 0 the more symmetric it is
lowestGrid = deepcopy(robots)
lowestTime = 0
time = 0
while time < 101*103: # The robots repeat positions every 101*103 seconds
    linePositions = {i:set() for i in range(limits[1])}
    for robot in robots:
        robot["p"] = tuple((robot["p"][i] + robot["v"][i])%limits[i] for i in range(2))
        linePositions[robot["p"][1]].add(robot["p"][0])
    time += 1
    xMean = sum([robot["p"][0] for robot in robots])/len(robots)
    symScore = 0
    for line in linePositions.values():
        symScore += sum([p-xMean for p in line])
    if abs(symScore) < lowestSymScore:
        lowestSymScore = abs(symScore)
        lowestTime = time
        lowestGrid = deepcopy(robots)
grid = [["." for _ in range(limits[0])] for _ in range(limits[1])]
for robot in lowestGrid:
    grid[robot["p"][1]][robot["p"][0]] = "X"
print(lowestTime)
print("\n".join(["".join(line) for line in grid]))