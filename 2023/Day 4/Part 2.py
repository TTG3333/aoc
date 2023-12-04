with open("Input.txt", "tr") as F:
    lines = F.read().splitlines()

cards = {i:1 for i in range(len(lines))}
for i, line in enumerate(lines):
    interesting = line.split(": ")[1]
    winning, mine = interesting.split(" | ")
    winning = {int(x) for x in winning.split(" ") if x != ""}
    mine = {int(x) for x in mine.split(" ") if x != ""}
    match = winning&mine
    for k in range(i+1, i+1+len(match)):
        cards[k] += cards[i]
print(sum(cards.values()))