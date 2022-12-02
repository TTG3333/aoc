with open("Input.txt", "tr") as F:
    data = F.read()
floor = 0
for char in data:
    if char == "(":
        floor += 1
    elif char == ")":
        floor -= 1
print(floor)