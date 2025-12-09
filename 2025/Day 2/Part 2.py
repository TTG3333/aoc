with open("Input.txt", "tr") as F:
    ranges = F.readline().split(",")

total = 0
for r in ranges:
    start, end = map(int, r.split("-"))
    for i in range(start, end + 1):
        istr = str(i)
        ilen = len(istr)
        for k in range(1, ilen):
            if ilen % k == 0:
                segment = istr[0:k]
                if segment * (ilen // k) == istr:
                    total += i
                    break
print(total)