import re

with open("Input.txt", "tr") as F:
    strings = F.read().splitlines()

total = 0
for s in strings:
    total -= len(s)
    s = s.replace(r'"', "a"*2)
    s = re.sub(r"\\x[0-9a-f]{2}", "a"*5, s)
    s = s.replace("\\", "a"*2)
    total += len(s) + 2
print(total)