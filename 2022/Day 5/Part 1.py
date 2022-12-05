from string import digits, ascii_uppercase

with open("Input.txt", "tr") as F:
    lines = F.read().splitlines()
for i, line in enumerate(lines):
    if line.startswith("move"):
        insts = lines[i:]
        stackLines = lines[i-3::-1]
        numCols = max([int(x) for x in lines[i-2] if x in digits])
        break
stacks = [[] for _ in range(numCols)]
for line in stackLines:
    for i in range(numCols):
        if line[4*i+1] in ascii_uppercase:
            stacks[i].append(line[4*i+1])

for inst in insts:
    inst = inst.replace("move ", "").replace("from ", "").replace("to ", "")
    num, orig, dest = [int(x) for x in inst.split(" ")]
    for _ in range(num):
        stacks[dest-1].append(stacks[orig-1].pop())
print("".join([x[-1] for x in stacks]))