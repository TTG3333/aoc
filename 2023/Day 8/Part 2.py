from math import lcm

with open("Input.txt", "tr") as F:
    lines = F.read().splitlines()

instructions = lines[0]
lines = lines[2:]
graph = {}
startingVals = []
for line in lines:
    start, ends = line[:-1].split(" = (")
    ends = ends.split(", ")
    graph[start] = ends.copy()
    if start[-1] == "A":
        startingVals.append(start)

counters = []
for val in startingVals:
    counter = 0
    while val[-1] != "Z":
        inst = instructions[counter % len(instructions)]
        val = graph[val][0] if inst == "L" else graph[val][1]
        counter += 1
    counters.append(counter)

print(lcm(*counters))