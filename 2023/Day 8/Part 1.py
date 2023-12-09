with open("Input.txt", "tr") as F:
    lines = F.read().splitlines()

instructions = lines[0]
lines = lines[2:]
graph = {}
for line in lines:
    start, ends = line[:-1].split(" = (")
    ends = ends.split(", ")
    graph[start] = ends.copy()

currentVal = "AAA"
end = "ZZZ"
counter = 0
while currentVal != end:
    inst = instructions[counter % len(instructions)]
    currentVal = graph[currentVal][0] if inst == "L" else graph[currentVal][1]
    counter += 1

print(counter)