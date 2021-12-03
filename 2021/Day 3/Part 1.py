with open("Input.txt", "tr") as F:
    bins = [x[::-1] for x in F.read().splitlines()]
bitCount = [{0: 0, 1: 0} for x in range(len(bins[0]))]
for x in bins:
    for y, bit in enumerate(x):
        if bit == "0":
            bitCount[y][0] += 1
        else:
            bitCount[y][1] += 1
gamma = epsilon = ""
for x in bitCount:
    if x[0] > x[1]:
        gamma += "0"
        epsilon += "1"
    else:
        gamma += "1"
        epsilon += "0"
gamma, epsilon = int(gamma[::-1], base=2), int(epsilon[::-1], base=2)
print(gamma*epsilon)