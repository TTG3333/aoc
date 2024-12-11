with open("Input.txt", "tr") as F:
    stones = [int(x) for x in F.read().split(" ")]

memo = {} # key will be stone number, value will be a dict with the key representing remaining blinks and the value the size of the produced stones

def getFuture(stone, blinks):
    if blinks == 0:
        return 1
    if stone in memo and blinks in memo[stone]:
        return memo[stone][blinks]
    count = 0
    if stone == 0:
        count += getFuture(1, blinks - 1)
    elif len(str(stone)) % 2 == 0:
        size = len(str(stone))
        count += getFuture(int(str(stone)[:size//2]), blinks - 1)
        count += getFuture(int(str(stone)[size//2:]), blinks - 1)
    else:
        count += getFuture(stone * 2024, blinks - 1)
    if stone in memo:
        memo[stone][blinks] = count
    else:
        memo[stone] = {blinks: count}
    return count

total = 0
for stone in stones:
    total += getFuture(stone, 75)
print(total)