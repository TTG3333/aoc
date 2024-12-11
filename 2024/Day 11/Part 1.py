with open("Input.txt", "tr") as F:
    stones = [int(x) for x in F.read().split(" ")]

for _ in range(25):
    newStones = []
    for stone in stones:
        if stone == 0:
            newStones.append(1)
        elif len(str(stone))%2 == 0:
            size = len(str(stone))
            newStones.append(int(str(stone)[:size//2]))
            newStones.append(int(str(stone)[size//2:]))
        else:
            newStones.append(stone * 2024)
    stones = newStones
print(len(stones))