import datetime

def find_arrangements(joltage, final_joltage, adapters):
    arrangements = 0
    if joltage == final_joltage - 3:
        return 1
    for y, x in enumerate(adapters[:3]):
        if x - joltage > 0 and x - joltage < 4:
            arrangements += find_arrangements(x, final_joltage, adapters[y + 1:])
        elif x - joltage > 3:
            break
    return arrangements

start_time = datetime.datetime.now()
print(start_time)
with open("Input.txt", "tr") as F:
    adapters = F.read().splitlines()
fixed_adapters = []
for y, x in enumerate(adapters):
    fixed_adapters.append(int(x))
fixed_adapters.sort()
start_joltage = 0
final_joltage = fixed_adapters[-1] + 3
answer = find_arrangements(start_joltage, final_joltage, fixed_adapters)
print(datetime.datetime.now() - start_time)
print(answer)