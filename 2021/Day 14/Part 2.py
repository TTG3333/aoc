with open("Input.txt", "tr") as F:
    data = F.read().splitlines()

pattern = {}
count = {}
for y, x in enumerate(data[0][:-1]):
    if x + data[0][y+1] in list(pattern.keys()):
        pattern[x + data[0][y+1]] += 1
    else:
        pattern[x + data[0][y+1]] = 1
    if x in list(count.keys()):
        count[x] += 1
    else:
        count[x] = 1
if data[0][-1] in list(count.keys()):
    count[data[0][-1]] += 1
else:
    count[data[0][-1]] = 1
rules = {x.split(" -> ")[0]: x.split(" -> ")[1] for x in data[2:]}

for _ in range(40):
    temp = pattern.copy()
    for key, value in pattern.items():
        if key in list(rules.keys()):
            if rules[key] in list(count.keys()):
                count[rules[key]] += value
            else:
                count[rules[key]] = value
            if key[0] + rules[key] in list(temp.keys()):
                temp[key[0] + rules[key]] += value
            else:
                temp[key[0] + rules[key]] = value
            if rules[key] + key[1] in list(temp.keys()):
                temp[rules[key] + key[1]] += value
            else:
                temp[rules[key] + key[1]] = value
            temp[key] -= value
    pattern = temp.copy()

print(max(list(count.values())) - min(list(count.values())))