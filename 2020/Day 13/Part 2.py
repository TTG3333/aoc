with open("Input.txt", "tr") as F:
    buses = [int(x) if x != "x" else None for x in F.read().splitlines()[1].split(",")]

increment = 1
counter = increment
for y, x in enumerate(buses):
    if x == None:
        continue
    while (counter + y) % x != 0:
        counter += increment
    increment *= x

print(counter)