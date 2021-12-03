with open("Input.txt", "tr") as F:
    inst = [x.split(" ") for x in F.read().splitlines()]
depth = horizontal = 0
for x in inst:
    if x[0] == "forward":
        horizontal += int(x[1])
    elif x[0] == "down":
        depth += int(x[1])
    elif x[0] == "up":
        depth -= int(x[1])
print(depth*horizontal)