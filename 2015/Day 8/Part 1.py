import re

with open("Input.txt", "tr") as F:
    strings = F.read().splitlines()

total = 0
for s in strings:
    total += len(s)
    s = s[1:-1]
    s = s.replace(r'\"', "a")
    s = re.sub(r"\\x[0-9a-f]{2}", "a", s)
    s = s.replace("\\\\", "a")
    total -= len(s)
print(total)