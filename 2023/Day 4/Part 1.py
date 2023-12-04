with open("Input.txt", "tr") as F:
    lines = F.read().splitlines()

total = 0
for line in lines:
    interesting = line.split(": ")[1]
    winning, mine = interesting.split(" | ")
    winning = {int(x) for x in winning.split(" ") if x != ""}
    mine = {int(x) for x in mine.split(" ") if x != ""}
    match = winning&mine
    total += 2**(len(match)-1) if len(match) > 0 else 0
print(total)