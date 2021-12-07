with open("Input.txt", "tr") as F:
    crabs = [int(x) for x in F.read().split(",")]

minVal, maxVal = min(crabs), max(crabs)
lowest = float("inf")
for x in range(minVal, maxVal):
    val = 0
    for crab in crabs:
        n = abs(crab-x)
        val += (n**2+n)//2
    if val < lowest:
        lowest = val
print(lowest)