with open("Input.txt", "tr") as F:
    lines = F.read().splitlines()

def product(*args):
    total = 1
    for item in args:
        total *= item
    return total

total = 0
for line in lines:
    game_part = line.split(": ")[1]
    minimums = {"red": 0, "green":0, "blue": 0}
    for play in game_part.split("; "):
        for colour in play.split(", "):
            num, col = colour.split(" ")
            num = int(num)
            if num > minimums[col]:
                minimums[col] = num
    total += product(*minimums.values())
print(total)