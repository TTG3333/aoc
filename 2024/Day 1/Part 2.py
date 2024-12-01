with open("Input.txt", "tr") as F:
    lines = F.read().splitlines()

left = []
right = []
for line in lines:
    half = line.split("   ")
    left.append(int(half[0]))
    right.append(int(half[1]))

total = 0
for x in left:
    total += x * right.count(x)

print(total)