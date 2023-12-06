from math import floor, ceil, sqrt

with open("Input.txt", "tr") as F:
    lines = F.read().splitlines()

time, distance = [int(x.split(": ")[1].replace(" ", "")) for x in lines]

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
print(int(last-first+1))