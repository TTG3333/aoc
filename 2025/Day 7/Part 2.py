def add_dict(dict, pos, count):
    if pos in dict:
        dict[pos] += count
    else:
        dict[pos] = count

with open("Input.txt", "tr") as F:
    lines = F.read().splitlines()

positions = {lines[0].index("S"):1}
for line in lines[1:]:
    new_positions = {}
    for pos, count in positions.items():
        if line[pos] == ".":
            add_dict(new_positions, pos, count)
        elif line[pos] == "^":
            add_dict(new_positions, pos - 1, count)
            add_dict(new_positions, pos + 1, count)
    positions = new_positions
print(sum(positions.values()))