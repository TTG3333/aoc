with open("Input.txt", "tr") as F:
    pairs = F.read().splitlines()

total = 0
for pair in pairs:
    elves = [[int(y) for y in x.split("-")] for x in pair.split(",")]
    elf1, elf2 = [set(range(x[0], x[1]+1)) for x in elves]
    if elf1 & elf2 == min(elf1, elf2, key=lambda a: len(a)):
        total += 1
print(total)