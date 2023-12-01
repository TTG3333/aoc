from string import digits

with open("Input.txt", "tr") as F:
    lines = F.read().splitlines()
total = 0
for line in lines:
    for char in line:
        if char in digits:
            total += 10*int(char)
            break
    for char in line[::-1]:
        if char in digits:
            total += int(char)
            break
print(total)