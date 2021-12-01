with open("Input.txt", "tr") as F:
    numbers = [int(x) for x in F.read().splitlines()]
sums = [x + numbers[y+1] + numbers[y+2] for y, x in enumerate(numbers[:-2])]
count = 0
for y, x in enumerate(sums[1:], start=1):
    if x > sums[y-1]:
        count += 1
print(count)