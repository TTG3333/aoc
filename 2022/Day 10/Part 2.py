with open("Input.txt", "tr") as F:
    insts = F.read().splitlines()

x = 1
cycle = 1
screen = [["."]*40 for _ in range(6)]
for inst in insts:
    if inst == "noop":
        toAdd = 1
    else:
        toAdd = 2
    for _ in range(toAdd):
        drawPos = (cycle-1)%40
        if x <= drawPos + 1 and x >= drawPos - 1:
            screen[(cycle-1)//40][(cycle-1)%40] = "#"
        cycle += 1
    if inst.startswith("addx"):
        x += int(inst.split(" ")[1])
for line in screen:
    print("".join(line))