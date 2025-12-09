with open("Input.txt", "tr") as F:
    ranges = F.readline().split(",")

total = 0
for r in ranges:
    start, end = map(int, r.split("-"))
    for i in range(start, end + 1):
        istr = str(i)
        if len(istr) % 2 == 0:
            first, second = istr[: len(istr) // 2], istr[len(istr) // 2 :]
            if first == second:
                total += i
print(total)