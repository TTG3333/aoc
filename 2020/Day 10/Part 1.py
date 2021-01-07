with open("Input.txt", "tr") as F:
    adapters = F.read().splitlines()
fixed_adapters = []
for y, x in enumerate(adapters):
    fixed_adapters.append(int(x))
fixed_adapters.sort()
diffs = {
    "1volt": 0,
    "3volt": 0
}
current_joltage = 0
for x in fixed_adapters:
    if x - current_joltage == 1:
        diffs["1volt"] += 1
    elif x - current_joltage == 3:
        diffs["3volt"] += 1
    current_joltage = x
diffs["3volt"] += 1
print(diffs["1volt"] * diffs["3volt"])