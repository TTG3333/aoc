with open("Input.txt", "tr") as F:
    lines = F.read().splitlines()

splits = 0
positions = {lines[0].index("S")}
for line in lines[1:]:
    new_positions = set()
    for pos in positions:
        if line[pos] == ".":
            new_positions.add(pos)
        elif line[pos] == "^":
            splits += 1
            new_positions.add(pos - 1)
            new_positions.add(pos + 1)
    positions = new_positions
print(splits)