with open("Input.txt", "tr") as F:
    lines = F.read().splitlines()
maximums = {"red": 12, "green": 13, "blue": 14}

total = 0
for line in lines:
    id_part, game_part = line.split(": ")
    id = int(id_part.split(" ")[1])
    for play in game_part.split("; "):
        for colour in play.split(", "):
            num, col = colour.split(" ")
            num = int(num)
            if num > maximums[col]:
                break
        else:
            continue
        break
    else:
        total += id
print(total)