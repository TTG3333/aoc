with open("Input.txt", "tr") as F:
    numbers = [int(x) for x in F.read().splitlines()]
count = 0
for y, x in enumerate(numbers[1:], start=1):
    if x > numbers[y-1]:
        count += 1
print(count)