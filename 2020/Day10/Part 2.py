def zeroCheck(val):
    if val < 0:
        return 0
    return val

with open("Input.txt", "tr") as F:
    adapters = F.read().splitlines()
fixed_adapters = [0]
for y, x in enumerate(adapters):
    fixed_adapters.append(int(x))
fixed_adapters.sort(reverse=True)
adapter_data = {}
for y, x in enumerate(fixed_adapters):
    arrangements = 0
    if y == 0:
        adapter_data[x] = 1
        continue
    for z in fixed_adapters[zeroCheck(y-3):y]:
        if z - x > 0 and z - x < 4:
            arrangements += adapter_data[z]
    adapter_data[x] = arrangements
print(adapter_data[0])