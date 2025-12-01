with open("Input.txt", "tr") as F:
    lines = F.read().splitlines()

pos = 50
count = 0
for line in lines:
    direction = line[0]
    steps = int(line[1:])
    if direction == "R":
        pos += steps
    elif direction == "L":
        pos -= steps
    pos %= 100
    if pos == 0:
        count += 1
print(count)