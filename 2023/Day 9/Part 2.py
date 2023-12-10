with open("Input.txt", "tr") as F:
    lines = F.read().splitlines()

total = 0
for line in lines:
    values = [int(x) for x in line.split(" ")[::-1]]
    diffs = [values.copy()]
    zeroes = False
    while not zeroes:
        zeroes = True
        diff = []
        for i in range(len(diffs[-1][:-1])):
            d = diffs[-1][i] - diffs[-1][i+1]
            if zeroes and d != 0:
                zeroes = False
            diff.append(d)
        diffs.append(diff)
    diffs[-1].append(0)
    for i in range(len(diffs)-2, -1, -1):
        diffs[i].append(diffs[i][-1]-diffs[i+1][-1])
    total += diffs[0][-1]
print(total)