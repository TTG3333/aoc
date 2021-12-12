with open("Input.txt", "tr") as F:
    data = F.read().splitlines()

fields = []
for y, line in enumerate(data):
    if line == "":
        fieldEnd = y + 1
        break
    vals = line.split(": ")
    field = {"name": vals[0]}
    vals = [[int(y) for y in x.split("-")] for x in vals[1].split(" or ")]
    field["vals"] = list(vals)
    fields.append(field)

for x, field in enumerate(fields):
    fields[x]["indices"] = {y: None for y in range(len(fields))}

validTickets = []
tickets = [[int(y) for y in x.split(",")] for x in data[fieldEnd + 4:]]
for ticket in tickets:
    for value in ticket:
        for field in fields:
            if (value >= field["vals"][0][0] and value <= field["vals"][0][1]) or (value >= field["vals"][1][0] and value <= field["vals"][1][1]):
                break
        else:
            break
    else:
        validTickets.append(ticket)

for ticket in validTickets:
    for index, value in enumerate(ticket):
        for x, field in enumerate(fields):
            if (value >= field["vals"][0][0] and value <= field["vals"][0][1]) or (value >= field["vals"][1][0] and value <= field["vals"][1][1]):
                if field["indices"][index] == None:
                    fields[x]["indices"][index] = True
            else:
                fields[x]["indices"][index] = False

indices = {field["name"]: None for field in fields}
while None in list(indices.values()):
    for field in fields:
        if list(field["indices"].values()).count(True) == 1:
            index = list(field["indices"].values()).index(True)
            for x in range(len(fields)):
                fields[x]["indices"][index] = False
            indices[field["name"]] = index
            break

ownTicket = [int(x) for x in data[fieldEnd + 1].split(",")]
fixedTicket = {}
for key, value in indices.items():
    fixedTicket[key] = ownTicket[value]

def multiply(L):
    count = 1
    for x in L:
        count *= x
    return count

print(multiply([value for key, value in fixedTicket.items() if "departure" in key]))