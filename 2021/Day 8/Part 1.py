with open("Input.txt", "tr") as F:
    nums = [[[z for z in y.split(" ")] for y in x.split(" | ")] for x in F.read().splitlines()]

count = 0
validLens = [2, 3, 4, 7]
for x in nums:
    x = x[1]
    for num in x:
        if len(num) in validLens:
            count += 1
print(count)