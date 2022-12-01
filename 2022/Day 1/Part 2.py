with open("Input.txt", "tr") as F:
    lines = F.read().splitlines()
elves = []
total = 0
for line in lines:
    if line == "":
        elves.append(total)
        total = 0
    else:
        total += int(line)
elves.append(total)
elves = sorted(elves, reverse=True)
print(sum([elves[i] for i in range(3)]))