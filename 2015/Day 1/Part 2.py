with open("Input.txt", "tr") as F:
    data = F.read()
floor = 0
for i, char in enumerate(data, start=1):
    if char == "(":
        floor += 1
    elif char == ")":
        floor -= 1
    if floor < 0:
        break
print(i)