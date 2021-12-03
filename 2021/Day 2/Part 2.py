with open("Input.txt", "tr") as F:
    inst = [x.split(" ") for x in F.read().splitlines()]
depth = horizontal = aim = 0
for x in inst:
    val = int(x[1])
    if x[0] == "forward":
        horizontal += val
        depth += aim*val
    elif x[0] == "down":
        aim += val
    elif x[0] == "up":
        aim -= val
print(depth*horizontal)