with open("Input.txt", "tr") as F:
    fishes = [int(x) for x in F.read().split(",")]

fishCount = {x: 0 for x in range(9)}
for x in fishes:
    fishCount[x] += 1
for x in range(256):
    fishCount[0], fishCount[1], fishCount[2], fishCount[3], fishCount[4], fishCount[5], fishCount[6], fishCount[7], fishCount[8] = fishCount[1], fishCount[2], fishCount[3], fishCount[4], fishCount[5], fishCount[6], fishCount[7]+fishCount[0], fishCount[8], fishCount[0]

print(sum(list(fishCount.values())))