from string import ascii_letters

with open("Input.txt", "tr") as F:
    sacks = F.read().splitlines()

total = 0
for sack in sacks:
    first, second = {x for x in sack[:len(sack)//2]}, {x for x in sack[len(sack)//2:]}
    common = first & second
    total += ascii_letters.find(common.pop())+1
print(total)