with open("Input.txt", "tr") as F:
    lines = F.read().splitlines()

pos = 50
count = 0
for line in lines:
    direction = line[0]
    steps = int(line[1:])
    for _ in range(steps):
        if direction == "R":
            pos += 1
        elif direction == "L":
            pos -= 1
        pos %= 100
        if pos == 0:
            count += 1
print(count)