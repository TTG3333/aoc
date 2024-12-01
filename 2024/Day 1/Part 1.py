with open("Input.txt", "tr") as F:
    lines = F.read().splitlines()

left = []
right = []
for line in lines:
    half = line.split("   ")
    left.append(int(half[0]))
    right.append(int(half[1]))

left = sorted(left)
right = sorted(right)

total = 0
for i in range(len(left)):
    total += abs(right[i] - left[i])

print(total)