from math import prod
import re

with open("Input.txt", "tr") as F:
    lines = F.read().splitlines()

seconds = 100
limits = [101, 103]
quadrants = [0]*4 # UL, UR, BL, BR
for line in lines:
    matches = [int(x) for x in re.match(r"^p=([\d-]+),([\d-]+) v=([\d-]+),([\d-]+)$", line).groups()]
    position = matches[0], matches[1]
    velocity = matches[2], matches[3]
    endPos = [(position[i] + seconds*velocity[i])%limits[i] for i in range(2)]
    quadrant = 0
    if endPos[0] > limits[0]//2: # Right half
        quadrant += 1
    elif endPos[0] == limits[0]//2: # In the middle
        continue
    if endPos[1] > limits[1]//2: # Bottom half
        quadrant += 2
    elif endPos[1] == limits[1]//2: # In the middle
        continue
    quadrants[quadrant] += 1
print(prod(quadrants))