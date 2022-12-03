from string import ascii_letters

with open("Input.txt", "tr") as F:
    sacks = F.read().splitlines()

total = 0
for g in range(0, len(sacks)-2, 3):
    first, second, third = [{x for x in sacks[g+i]} for i in range(3)]
    common = first & second & third
    total += ascii_letters.find(common.pop())+1
print(total)