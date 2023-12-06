from math import floor, ceil, sqrt

with open("Input.txt", "tr") as F:
    lines = F.read().splitlines()

times, distances = [[int(x) for x in y.split(": ")[1].split(" ") if x != ""] for y in lines]

total = 1
for i, time in enumerate(times):
    distance = distances[i]
    time1 = -(-time-sqrt(time**2-4*distance))/2
    time2 = -(-time+sqrt(time**2-4*distance))/2
    first = min(time1, time2)
    last = max(time1, time2)
    if first % 1 == 0:
        first += 1
    else:
        first = ceil(first)
    if last % 1 == 0:
        last -= 1
    else:
        last = floor(last)
    total *= int(last-first+1)
print(total)