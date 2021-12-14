with open("Input.txt", "tr") as F:
    data = F.read().splitlines()

pattern = [x for x in data[0]]
rules = {x.split(" -> ")[0]: x.split(" -> ")[1] for x in data[2:]}

for _ in range(10):
    temp = pattern.copy()
    offset = 0
    for y, x in enumerate(pattern[:-1]):
        if x + pattern[y+1] in list(rules.keys()):
            temp.insert(y+offset+1, rules[x+pattern[y+1]])
            offset += 1
    pattern = temp.copy()

count = {}
for x in pattern:
    if x not in list(count.keys()):
        count[x] = 1
    else:
        count[x] += 1

print(max(list(count.values())) - min(list(count.values())))