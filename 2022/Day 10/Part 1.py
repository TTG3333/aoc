with open("Input.txt", "tr") as F:
    insts = F.read().splitlines()

x = 1
cycle = 1
total = 0
for inst in insts:
    if inst == "noop":
        toAdd = 1
    else:
        toAdd = 2
    for _ in range(toAdd):
        if cycle % 40 == 20 and cycle <= 220:
            total += x * cycle
        cycle += 1
    if inst.startswith("addx"):
        x += int(inst.split(" ")[1])
print(total)