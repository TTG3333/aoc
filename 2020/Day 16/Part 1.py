with open("Input.txt", "tr") as F:
    data = F.read().splitlines()

fields = []
for y, line in enumerate(data):
    if line == "":
        fieldEnd = y + 1
        break
    vals = line.split(": ")[1].split(" or ")
    vals = [[int(y) for y in x.split("-")] for x in vals]
    fields.append(vals)

errorRate = 0
tickets = [[int(y) for y in x.split(",")] for x in data[fieldEnd + 4:]]
for ticket in tickets:
    for value in ticket:
        for field in fields:
            if (value >= field[0][0] and value <= field[0][1]) or (value >= field[1][0] and value <= field[1][1]):
                break
        else:
            errorRate += value

print(errorRate)